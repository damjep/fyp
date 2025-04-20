<template>
    <div class="card">
      <div class="card-header">
        <div class="nav nav-tabs" id="nav-tab" role="tablist">
          <button
            class="nav-link"
            :class="{ active: index === 0 }"
            v-for="(items, index) in menuData"
            :key="'tab-btn-' + index"
            :id="'tab-' + index"
            data-bs-toggle="tab"
            :data-bs-target="'#tab-pane-' + index"
            type="button"
            role="tab"
            :aria-controls="'tab-pane-' + index"
            :aria-selected="index === 0 ? 'true' : 'false'"
          >
            {{ items.dish_type }}
          </button>
        </div>
      </div>
  
      <div class="tab-content card-body" id="nav-tabContent"
       style="overflow-y: auto; max-height: 25vh;">
        <div
          class="tab-pane fade"
          :class="{ show: index === 0, active: index === 0 }"
          v-for="(items, index) in menuData"
          :key="'tab-content-' + index"
          :id="'tab-pane-' + index"
          role="tabpanel"
          :aria-labelledby="'tab-' + index"
          tabindex="0"
        >
        <div v-for="(item, category) in items.extra_dish_types">
            <h1>{{ category }}</h1>
            <table class="table">
                <thead>
                    <th>Dish</th>
                    <th>Quantity</th>
                    <th>Add ?</th>
                </thead>
                <tbody>
                    <tr v-for="dish in item" :key="dish.id">
                        <td>{{ dish.name }}</td>
                        <td>
                          <div class="mb-3 row">
                            <div class="col-sm-10">
                              <input type="number" class="form-control" 
                              min="0"
                              v-model="dish.quantity">
                            </div>
                          </div>
                        </td>
                        <td>
                            <button class="btn btn-primary"
                            @click="addOrderItems(order_id, dish.id, dish.quantity)">
                                +
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
            
        </div>
      </div>
    </div>
  </template>
  
  <script setup lang="ts">
  import axios from 'axios'
  import { onMounted, ref } from 'vue'
  
  const emit = defineEmits(['item-added'])

  const props = defineProps<{
    order_id: number,
  }>()

  const menuData = ref()
  
  async function fetchMenuData() {
    try {
      const res = await axios.get('api/get-menu')
      menuData.value = res.data
    } catch (err) {
      console.error(err)
    }
  }
  
  async function addOrderItems(orderID: number, dish_id: number, q: number){
    try {
        const res = await axios.post(`/pos-api/${orderID}/items/`, {
            dish: dish_id,
            quantity: q,
        },{
            withCredentials: true
        })

        emit('item-added')
        await fetchMenuData()
    } catch (err) {

    }
  }

  

  onMounted(fetchMenuData)
  </script>
  