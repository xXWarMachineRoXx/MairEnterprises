<template>
    <div class="flex">
      <div class="col">
        <!-- Pass isOpen as a prop and listen to the 'update:isOpen' event -->
        <Modal :is-open="isOpen" @update:is-open="updateIsOpen" />
      </div>
      <div class="col">
        <!-- Button to open the modal -->
        <SfButton @click="open"><SfIconSearch /></SfButton>
      </div>
    </div>
  </template>
  
  <script lang="ts" setup>
  import Modal from '../components/Molecules/Modal/Modal.vue';
  import { SfButton, useDisclosure,SfIconSearch } from '@storefront-ui/vue';
  
  // useDisclosure is a composable that manages the open state
  const { isOpen, open, close } = useDisclosure({ initialValue: false });
  
  // This method updates the isOpen state when the modal emits an update
  const updateIsOpen = (newIsOpen:Boolean) => {
    if (newIsOpen) {
      open();
    } else {
      close();
    }
  };
  </script>
  