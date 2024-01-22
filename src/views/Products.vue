<template class="!bg-primary-500">
  <Navbar />
  <div class="mx-12 my-8 p-4">
    <Breadcrumbs />
    <h1 class="font-bold text-4xl"> Browse Products </h1>
    <div class="flex gap-6">
      <FilterSideBar />
      <div class="flex flex-col gap-8">
        <h2 class="font-bold text-lg"> All Products </h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
          <ProductCard v-for="product in products" :key="product.id" :img="product.img" :alt="product.alt"
            :productName="product.productName" :price="product.price" :description="product.description"
            :numberofReviews="product.numberofReviews" :category="product.category" :canWishlist="product.canWishlist" :averageRating="product.averageRating" :productLink="product.productLink" />
        </div>
        <Pagination />
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Navbar from '../components/Organisms/Navbar/Navbar.vue';
import Breadcrumbs from '../components/Molecules/Breadcrumbs/Breadcrumbs.vue';
import FilterSideBar from '../components/Organisms/FilterSideBar/FilterSideBar.vue';
import ProductCard from '../components/Molecules/ProductCard/ProductCard.vue';
import Pagination from '../components/Molecules/Pagination/Pagination.vue';
import benq from '@/assets/images/benq.png';
import benqth685p from '@/assets/images/products/benq-th685p-projector-500x500.png';

export default defineComponent({
  data() {
    return {
      // Array of product objects
      products: [
        {
          "id": 1,
          "img": benq,
          "alt": "BenQ EH600 Smart Projector",
          "category": "Top Rated",
          "numberofReviews": 15,
          "averageRating": 4,
          "productName": "BenQ EH600 Smart Projector",
          "canWishlist": false,
          "price": "74,900",
          "productLink": "BenQ-EH600-Smart-Projector",
          "description": "Advanced smart projector with high-resolution display."
        },
        {
          "id": 2,
          "img": benqth685p,
          "alt": "BenQ TH685P Projector",
          "category": "Top Rated",
          "numberofReviews": 25,
          "productName": "BenQ TH685P Projector",
          "price": "79,000",
          "description": "High-performance projector for gaming and home theater."
        },
        {
          "id": 3,
          "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361146632/PR/LF/AC/3098002/benq-mh560-projector-500x500.jpg",
          "alt": "BenQ MH560 Room Projector",
          "category": "Top Rated",
          "numberofReviews": 30,
          "productName": "BenQ MH560 Room Projector",
          "price": "59,990",
          "description": "Versatile room projector for both professional and personal use."
        },
        {
          "id": 4,
          "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361171059/UY/GL/RF/3098002/benq-tk700-projectors-500x500.jpg",
          "alt": "BenQ TK700 Projectors",
          "category": "Top Rated",
          "numberofReviews": 18,
          "productName": "BenQ TK700 Projectors",
          "price": "1,49,990",
          "description": "State-of-the-art projectors for an immersive viewing experience."
        },
        {
          "id": 5,
          "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361153340/RI/MR/XX/3098002/benq-eh620-projector-500x500.jpg",
          "alt": "BenQ EH620 Projector",
          "category": "Top Rated",
          "numberofReviews": 22,
          "productName": "BenQ EH620 Projector",
          "price": "1,21,000",
          "description": "Innovative projector with exceptional clarity and brightness."
        },
        {
          "id": 6,
          "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361168694/GL/CT/RX/3098002/benq-ex600-projector-500x500.jpg",
          "alt": "BenQ EX600 Projector",
          "category": "Top Rated",
          "numberofReviews": 12,
          "productName": "BenQ EX600 Projector",
          "price": "56,599",
          "description": "Compact and efficient projector, ideal for office and educational use."
        }, 
        {
          "id": 7,
          "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361169334/QG/KC/RO/3098002/benq-ms560p-projector-500x500.jpg",
          "alt": "BenQ MS560P Projector",
          "category": "Top Rated",
          "numberofReviews": 4,
          "productName": "BenQ MS560P Projector",
          "price": "32,500",
          "description": "Description of BenQ MS560P Projector"
        },
        {
          "id": 8,
          "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361149907/AF/CS/PO/3098002/benq-ms550-projector-500x500.jpg",
          "alt": "BenQ MS550 Meeting Room Projector",
          "category": "Top Rated",
          "numberofReviews": 79,
          "productName": "BenQ MS550 Meeting Room Projector",
          "price": "31,500",
          "description": "Description of BenQ MS550 Meeting Room Projector"
        },
        {
          "id": 9,
          "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361166848/JU/WX/KL/3098002/benq-mx808pst-projector-500x500.jpg",
          "alt": "BenQ MX808PST+ Projector",
          "category": "Top Rated",
          "numberofReviews": 63,
          "productName": "BenQ MX808PST+ Projector",
          "price": "50,000",
          "description": "Description of BenQ MX808PST+ Projector"
        },
        {
          "id": 10,
          "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361000660/QR/HV/IQ/3098002/xerox-photocopiers-500x500.jpg",
          "alt": "BenQ MX808STH Interactive Projector",
          "category": "Top Rated",
          "numberofReviews": 38,
          "productName": "BenQ MX808STH Interactive Projector",
          "price": "51,500",
          "description": "Description of BenQ MX808STH Interactive Projector"
        },
        {
          "id": 11,
          "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360999536/TT/DJ/HI/3098002/office-automation-service-500x500.jpg",
          "alt": "BenQ GS50 Potrable Projector",
          "category": "Top Rated",
          "numberofReviews": 84,
          "productName": "BenQ GS50 Potrable Projector",
          "price": "69,990",
          "description": "Description of BenQ GS50 Potrable Projector"
        },
        {
          "id": 12,
          "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361155103/FE/ZJ/LU/3098002/benq-th690st-projector-500x500.jpg",
          "alt": "BenQ Th690st Projector",
          "category": "Top Rated",
          "numberofReviews": 99,
          "productName": "BenQ Th690st Projector",
          "price": "1,09,990",
          "description": "Description of BenQ Th690st Projector"
        },
        {
          "id": 13,
          "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361155734/GD/MG/BT/3098002/benq-lw500st-projector-500x500.png",
          "alt": "BenQ LW500ST Projector",
          "category": "Top Rated",
          "numberofReviews": 29,
          "productName": "BenQ LW500ST Projector",
          "price": "54,990",
          "description": "Description of BenQ LW500ST Projector"
        },
        {
          "id": 14,
          "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361155968/BX/ZQ/JQ/3098002/benq-mx550-projector-500x500.jpg",
          "alt": "BenQ MX550 Projector",
          "category": "Top Rated",
          "numberofReviews": 76,
          "productName": "BenQ MX550 Projector",
          "price": "37,300",
          "description": "Description of BenQ MX550 Projector"
        },
        {
        "id": 15,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360399256/RV/OF/VK/3098002/viewsonic-ls751hd-projector-500x500.jpg",
        "alt": "ViewSonic LS751HD Projector",
        "category": "Top Rated",
        "numberofReviews": 98,
        "productName": "ViewSonic LS751HD Projector",
        "price": "2,80,000",
        "description": "Description of ViewSonic LS751HD Projector"
    },
    {
        "id": 16,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361135043/PQ/TQ/XD/3098002/viewsonic-ls550whe-projector-500x500.jpg",
        "alt": "ViewSonic LS550WHE Projector",
        "category": "Top Rated",
        "numberofReviews": 43,
        "productName": "ViewSonic LS550WHE Projector",
        "price": "61,500",
        "description": "Description of ViewSonic LS550WHE Projector"
    },
    {
        "id": 17,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134787/UB/QO/DR/3098002/viewsonic-cpb701hdh-projector-500x500.jpg",
        "alt": "ViewSonic CPB701HD Projector",
        "category": "Top Rated",
        "numberofReviews": 77,
        "productName": "ViewSonic CPB701HD Projector",
        "price": "62,299",
        "description": "Description of ViewSonic CPB701HD Projector"
    },
    {
        "id": 18,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360398543/CB/JA/KP/3098002/viewsonic-cpb701-4k-home-projector-500x500.jpg",
        "alt": "ViewSonic CPB701-4K Home Projector",
        "category": "Top Rated",
        "numberofReviews": 1,
        "productName": "ViewSonic CPB701-4K Home Projector",
        "price": "1,18,900",
        "description": "Description of ViewSonic CPB701-4K Home Projector"
    },
    {
        "id": 19,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360397098/JB/GH/QN/3098002/viewsonic-m1-g2-854x480-resolution-led-projecto-500x500.jpg",
        "alt": "ViewSonic M1+_G2 Smart  Portable Projector",
        "category": "Top Rated",
        "numberofReviews": 69,
        "productName": "ViewSonic M1+_G2 Smart  Portable Projector",
        "price": "46,000",
        "description": "Description of ViewSonic M1+_G2 Smart  Portable Projector"
    },
    {
        "id": 20,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360396412/PQ/GD/FC/3098002/viewsonic-pa503x-projector-500x500.jpg",
        "alt": "ViewSonic PA503X Projector",
        "category": "Top Rated",
        "numberofReviews": 56,
        "productName": "ViewSonic PA503X Projector",
        "price": "39,700",
        "description": "Description of ViewSonic PA503X Projector"
    },
    {
        "id": 21,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360395316/OG/GV/CK/3098002/viewsonic-pa503s-3-projector-500x500.jpg",
        "alt": "ViewSonic PA503S-3 Projector",
        "category": "Top Rated",
        "numberofReviews": 55,
        "productName": "ViewSonic PA503S-3 Projector",
        "price": "29,990",
        "description": "Description of ViewSonic PA503S-3 Projector"
    },
    {
        "id": 22,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134778/LR/AA/SS/3098002/egate-i9-pro-max-android-projector-500x500.jpg",
        "alt": "EGATE I9 Pro Max Android Projector",
        "category": "Top Rated",
        "numberofReviews": 76,
        "productName": "EGATE I9 Pro Max Android Projector",
        "price": "12,990",
        "description": "Description of EGATE I9 Pro Max Android Projector"
    },
    {
        "id": 23,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361073635/EB/RF/QY/3098002/egate-k9-pro-max-android-projector-500x500.jpg",
        "alt": "EGATE K9 Pro Max Android Projector",
        "category": "Top Rated",
        "numberofReviews": 37,
        "productName": "EGATE K9 Pro Max Android Projector",
        "price": "15,500",
        "description": "Description of EGATE K9 Pro Max Android Projector"
    },
    {
        "id": 24,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134831/VI/KS/AW/3098002/egate-l9-pro-android-projector-500x500.jpg",
        "alt": "EGATE L9 Pro Android Projector",
        "category": "Top Rated",
        "numberofReviews": 76,
        "productName": "EGATE L9 Pro Android Projector",
        "price": "21,990",
        "description": "Description of EGATE L9 Pro Android Projector"
    },
    {
        "id": 25,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360985723/WE/SX/AM/3098002/epson-digital-projector-500x500.jpg",
        "alt": "EGATE O9 Pro Zen Projector",
        "category": "Top Rated",
        "numberofReviews": 14,
        "productName": "EGATE O9 Pro Zen Projector",
        "price": "25,990",
        "description": "Description of EGATE O9 Pro Zen Projector"
    },
    {
        "id": 26,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134818/AQ/KW/TS/3098002/egate-o9-pro-automatic-smart-projector-500x500.jpg",
        "alt": "EGATE O9 Pro Automatic Smart Projector",
        "category": "Top Rated",
        "numberofReviews": 59,
        "productName": "EGATE O9 Pro Automatic Smart Projector",
        "price": "25,990",
        "description": "Description of EGATE O9 Pro Automatic Smart Projector"
    },
    {
        "id": 27,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/360394543/UM/LI/SZ/3098002/epson-eb-e01-xga-3lcd-projector-500x500.jpg",
        "alt": "Epson EB-E01 XGA 3LCD Projector",
        "category": "Top Rated",
        "numberofReviews": 5,
        "productName": "Epson EB-E01 XGA 3LCD Projector",
        "price": "33,333",
        "description": "Description of Epson EB-E01 XGA 3LCD Projector"
    },
    {
        "id": 28,
        "img": "https://5.imimg.com/data5/SELLER/Default/2023/11/361134899/HL/LB/BU/3098002/epson-co-fh02-lumen-projector-500x500.jpg",
        "alt": "Epson CO-FH02 Lumen Projector",
        "category": "Top Rated",
        "numberofReviews": 88,
        "productName": "Epson CO-FH02 Lumen Projector",
        "price": "80,000",
        "description": "Description of Epson CO-FH02 Lumen Projector"
    }
        // ... Continue with the rest of the entries in similar format
      ]
    };
  },

  components: { Navbar, Breadcrumbs, FilterSideBar, ProductCard, Pagination }
});

</script>
