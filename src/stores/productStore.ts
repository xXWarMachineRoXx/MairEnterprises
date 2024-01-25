import { defineStore } from 'pinia';
import allproducts from '../assets/helper/json/allproducts.json';

interface product {
  id: number,
  img: string,
  alt: string,
  category: string,
  brand: string,
  type: string,
  numberofReviews: number,
  canWishlist: boolean,
  averageRating: number,
  productName: string,
  productLink: string,
  price: string,
  description: string,
}


export const useProductsStore = defineStore('products', {
  // State is a function that returns an object containing your state properties
  state: () => ({
    products: allproducts,
    // filteredProducts: [],
    filterCriteria: {
      brand: '',
      priceRange: { min: 0, max: Infinity },
      type: '',
      minRating: 0,
    }
  }),
  // Actions are methods used to update the state
  actions: {
    addProduct(product: product) {
      this.products.push(product);
    },
    setFilterCriteria(criteria: {
      brand: string,
      priceRange: { min: number, max: number },
      type: string,
      minRating: number,
    }) {
      this.filterCriteria = criteria;
    },
  },
  // Getters are like computed properties for stores
  getters: {
    filteredProducts: (state) => {
      return state.products.filter(product => {
        var matchesBrand = state.filterCriteria.brand.split(', ').some(brand => product.brand.toLowerCase() === brand.toLowerCase());
        var withinPriceRange = parseInt(product.price.replace(/,/g, '')) >= state.filterCriteria.priceRange.min && 
                                 (!state.filterCriteria.priceRange.max || parseInt(product.price.replace(/,/g, '')) <= state.filterCriteria.priceRange.max);
        var meetsMinRating = product.averageRating >= state.filterCriteria.minRating;
    
        return matchesBrand && withinPriceRange && meetsMinRating;
      });
    },
    // New getter for brand counts based on filtered products
  brandCounts: (state) => {
    const counts = {};
    const filtered = state.products; // Use filtered products
    filtered.forEach((product :product) => {
      const brand = product.brand;
      if (!counts[brand]) {
        counts[brand] = 0;
      }
      counts[brand]++;
    });
    return counts;
  },
  // New getter for rating counts based on filtered products
  ratingCounts: (state) => {
    const counts = { '1': 0, '2': 0, '3': 0, '4': 0, '5': 0 };
    const filtered = state.filteredProducts; // Use filtered products
    filtered.forEach((product: product) => {
      const rating = Math.floor(product.averageRating);
      if (counts.hasOwnProperty(rating)) {
        counts[rating]++;
      }
    });
    return counts;
  },

  },
});
