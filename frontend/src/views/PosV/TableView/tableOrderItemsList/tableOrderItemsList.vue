<template>
    <div class="card" style="height: 30vh;">
        <div class="card-body">
            <div style="overflow-y: scroll; max-height: 50%;">
                <table class="table" >
                    <thead class="sticky-top">
                        <tr>
                            <th scope="col">Dish</th>
                            <th scope="col">Price</th>
                            <th scope="col">Quantity</th>
                            <th scope="col">Total</th>
                            <th></th>
                        </tr>
                    </thead>
                    
                    <tbody v-if="orderData" >
                        
                        <tr  v-for="items in orderData" 
                        :key="items.id">
                            <td>{{ items.dish_name }}</td>
                            <td>{{ items.price }}</td>
                            <td>{{ items.quantity }}</td>
                            <td>{{ items.total_price }}</td>
                            <td>
                                <button class="btn btn-danger"
                                @click="deleteOrderItems(items.order, items.id)">
                                    X
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { ref } from 'vue';

const emit = defineEmits(['item-deleted'])

const props = defineProps<{
    orderData: any;
}>()

                                    
async function deleteOrderItems(orderID: number, order_item_id: number){
    try {
      const res = await axios.delete(`pos-api/${orderID}/items/${order_item_id}`, {
        withCredentials: true
      })

      emit('item-deleted')

    } catch (err){}
  }
</script>