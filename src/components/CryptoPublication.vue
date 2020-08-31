<template>
  <div>
    <p>
      <!-- title -->
      <a :href="link"><b>{{ name }}</b></a>
      <span v-if="variants && variants.length">
        [
          <span
            v-for="(variant, variantIndex) in variants"
            v-bind="variant"
            :key="variant.name"
          >
            <a
              :href="variant.link">{{ variant.name }}</a>
            <span
              v-if="variantIndex < variants.length - 1"
            >, </span>
          </span>
        ]
      </span><br />

      <!-- authors -->
      <span
        v-for="(author, authorIndex) in authors"
        v-bind="author"
        :key="author.name"
      >
        <a v-if="author.link"
          :href="author.link">{{ author.name }}</a>
        <span v-else>{{ author.name }}</span>
        <span
          v-if="authorIndex < authors.length - 1"
        >, </span>
      </span><br />

      <!-- details -->
      <span
        v-if="archive"
        v-bind="archive">
        <span v-if="archive.link"><a :href="archive.link">{{ archive.name }}</a>, </span>
        <span v-else>{{ archive.name }}, </span>
      </span>
      <span v-if="details">{{ details }}</span>
    </p>
  </div>
</template>

<script>
export default {
  name: 'CryptoPublication',
  props: {
    name: {
      type: String,
      required: true
    },

    link: {
      type: String,
      default: ''
    },

    variants: {
      type: Array,
      default: () => []
    },

    authors: {
      type: Array,
      default: () => []
    },

    archive: {
      type: Object,
      default: () => null
    },

    details: {
      type: String,
      default: ''
    }
  }
}
</script>
