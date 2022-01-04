<template>
  <div>
    <p>
      <!-- name -->
      <b>{{ name }}</b><br />
      <span v-if="lectures && lectures.length">
        <span
          v-for="(lecture,lectureIndex) in lectures"
          v-bind="lecture"
          :key="lectureIndex"
        >
          {{ lecture.name }}
          [
          <span
            v-for="(variant, variantIndex) in lecture.variants"
            v-bind="variant"
            :key="variantIndex"
          >
            <a
              :href="variant.link">{{ variant.name }}</a>
            <span
              v-if="variantIndex < lecture.variants.length - 1"
            >, </span>
          </span>
        ]
        <br />
        </span>
      </span>

      <!-- teachers -->
      <span
        v-for="(person, personIndex) in teachers"
        v-bind="person"
        :key="personIndex"
      >
        <span>{{ person.name }}</span>
        <span
          v-if="personIndex < teachers.length - 1"
        >, </span>
      </span><br />

      <!-- semester -->
      <span>{{ semester }}</span><br />
    </p>
  </div>
</template>

<script>
export default {
  name: 'CryptoTeaching',
  props: {
    name: {
      type: String,
      required: true
    },

    lectures: {
      type: Array,
      default: () => []
    },

    teachers: {
      type: Array,
      default: () => []
    },

    semester: {
      type: String,
      required: true
    }
  }
}
</script>
