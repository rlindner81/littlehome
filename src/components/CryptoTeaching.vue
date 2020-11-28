<template>
  <div>
    <p>
      <!-- name -->
      <b>{{ name }}</b><br />
      <span v-if="lectures && lectures.length">
        <span
          v-for="(lecture,index) in lectures"
          v-bind="lecture"
          :key="index"
        >
          {{ lecture.name }}
          [
          <span
            v-for="(variant, index) in lecture.variants"
            v-bind="variant"
            :key="index"
          >
            <a
              :href="variant.link">{{ variant.name }}</a>
            <span
              v-if="index < lecture.variants.length - 1"
            >, </span>
          </span>
        ]
        <br />
        </span>
      </span>

      <!-- teachers -->
      <span
        v-for="(person, index) in teachers"
        v-bind="person"
        :key="index"
      >
        <span>{{ person.name }}</span>
        <span
          v-if="index < teachers.length - 1"
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
