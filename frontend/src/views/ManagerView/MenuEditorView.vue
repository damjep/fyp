<template>
    <div>
        <!-- Button trigger modal -->
        <button type="button" class="btn btn-primary" 
        data-bs-toggle="modal" data-bs-target="#exampleModal">
        Add Dish
        </button>

        <!-- Modal -->
        <div class="modal fade" id="exampleModal" 
        tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">Add Dish</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form @submit.prevent="addDish(dishAdd)">
                        <ul class="list-group list-group-horizontal ">
                            <li class="list-group-item" >
                                <div class="input-group flex-nowrap">
                                    <span class="input-group-text" id="addon-wrapping">Name</span>
                                    <input v-model="dishAdd.name" type="text" class="form-control"  aria-label="Username" aria-describedby="addon-wrapping">
                                </div>

                                <div class="input-group flex-nowrap">
                                    <span class="input-group-text" id="addon-wrapping">Price</span>
                                    <input v-model="dishAdd.price" 
                                    type="number" class="form-control" aria-label="Username" aria-describedby="addon-wrapping">
                                </div>
                            </li>

                            <li class="list-group-item"> 
                                <div class="input-group flex-nowrap">
                                    <span class="input-group-text" id="addon-wrapping">Description</span>
                                    <textarea v-model="dishAdd.description"
                                    type="textarea" class="form-control" :placeholder="dishAdd.description" aria-label="Username" aria-describedby="addon-wrapping"></textarea>
                                </div>
                            </li>
                        </ul>


                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary">Save changes</button>
                        </div>
                    </form>
                </div>
                </div>
            </div>
        </div>
    </div>

    <div v-if="menu" v-for="(items, category) in menu" >
        <h1>{{ category}}</h1>
        <div  v-for="item in items" :key="items.id">
            <h4>{{ item.extra_dish_type }}</h4>
            <div v-for="dish in item.dishes">
                <form @submit.prevent="editDish(dish.id, dish)">
                    <ul class="list-group list-group-horizontal ">
                        <li class="list-group-item" >
                            <div class="input-group flex-nowrap">
                                <span class="input-group-text" id="addon-wrapping">Name</span>
                                <input v-model="dish.name" type="text" class="form-control"  aria-label="Username" aria-describedby="addon-wrapping">
                            </div>

                            <div class="input-group flex-nowrap">
                                <span class="input-group-text" id="addon-wrapping">Price</span>
                                <input v-model="dish.price" 
                                type="number" class="form-control" :placeholder="dish.price" aria-label="Username" aria-describedby="addon-wrapping">
                            </div>
                        </li>

                        <li class="list-group-item"> 
                            <div class="input-group flex-nowrap">
                                <span class="input-group-text" id="addon-wrapping">Description</span>
                                <textarea v-model="dish.description"
                                type="textarea" class="form-control" :placeholder="dish.description" aria-label="Username" aria-describedby="addon-wrapping"></textarea>
                            </div>
                        </li>

                        <li class="list-group-item">
                            <button type="submit" class="btn btn-success">Save</button>

                            <span>
                            <button type="button" class="btn btn-danger" 
                            @click="deleteDish(dish.id)">Delete</button>
                        </span>
                        </li>
                    </ul>
                </form>
            </div>

        </div>

    </div>
</template>

<script setup lang="ts">
import axios from 'axios';
import { onMounted, ref } from 'vue';

const menu = ref()
const csrfToken = ref('')
const dishAdd = ref({
    name: '',
    price: 0,
    description: '',
})

async function addDish(dishAdd: any){
    try {
        const res = await axios.post('api/edit-dish/', {
            name: dishAdd.name,
            price: dishAdd.price.value,
            description: dishAdd.description.value,
        }, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken.value,
            },
            withCredentials: true,
        })
    } catch (err) {
        console.error(err);
    }
}

async function getToken() {
    try {
        const res = await axios.get('/api/get-token', {
            withCredentials: true,
        })
        csrfToken.value = res.data
    } catch (err) {
        console.error(err)
    }
}

async function fetchMenu(){
    try {
        const res = await axios.get('api/get-menu', {
            withCredentials: true, 
        })
        menu.value = res.data
        console.log(menu.value);
        
    } catch (err) {
        console.error(err)
    }
}

async function editDish(id: any, dish: any) {
    try {
        await getToken();
        const res = await axios.patch(`api/edit-dish/${id}`, {
            name: dish.name,
            price: dish.price,
            description: dish.description,
        }, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken.value,
            },
            withCredentials: true,
        })

        console.log(res.data);
        
    } catch (err) {
        console.error(err)
    }
}

async function deleteDish(id: any) {
    try {
        await getToken();
        const res = await axios.delete(`api/edit-dish/${id}`, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken.value,
            },
            withCredentials: true,
        })

        await fetchMenu();

        console.log(res.data);
        
    } catch (err) {
        console.error(err)
    }
}

onMounted(async () => {
    try {
        await fetchMenu();
    } catch (err) {
        console.error(err)
    };
})
</script>
