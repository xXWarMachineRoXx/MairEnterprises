<script>
import algoliasearch from 'algoliasearch/lite';
import 'instantsearch.css/themes/algolia-min.css';
import { getPropertyByPath } from 'instantsearch.js/es/lib/utils';

export default {
  data() {
    return {
      searchClient: algoliasearch(
          'VTS0EMFK4F',
          '720086cbe320183f28c76280b3293ce8'
      ),
    };
  },
  methods: {
    getPropertyByPath,
  },
};
</script>

<template>
  <ais-instant-search :search-client="searchClient" index-name="allproducts">
    <ais-configure :hits-per-page.camel="5"></ais-configure>
    <ais-search-box></ais-search-box>
    <ais-hits>
      <template v-slot:item="{ item }">
        <img :src="item.img" />
				<div class="hit-productName">
				  <ais-highlight attribute="productName" :hit="item"></ais-highlight>
				</div>
				<div class="hit-price">
				  <ais-highlight attribute="price" :hit="item"></ais-highlight>
				</div>
				<div class="hit-description">
				  <ais-highlight attribute="description" :hit="item"></ais-highlight>
				</div>
      </template>
    </ais-hits>
  </ais-instant-search>
</template>


<style>
.ais-SearchBox {
  margin-bottom: 1em;
}

.ais-InstantSearch {
  max-width: 960px;
  width: 100%;
  display: block;
  overflow: hidden;
  margin: 0 auto
}

.ais-Hits-item {
  margin-left: 0;
  width: 100%;
}

.ais-Hits-item img {
  margin-right: 1em
}

.ais-Hits-list {
  margin-bottom: 1em;
}
</style>