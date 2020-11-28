<template>
  <q-page class="flex-block">
    <div class="row q-pa-md q-col-gutter-md">
      <div class="col-12">
        <h4>
          Crypto
        </h4>

        <h5>
          Research Interests
        </h5>
        Cryptographic primitives and protocols resistant to quantum computer attacks. In particular, practical and provably secure schemes with weak hardness assumptions.

        <h5>
          Publications
        </h5>
        <CryptoPublication
          v-for="(publication, index) in publications"
          :key="index"
          v-bind="publication"
        ></CryptoPublication>

        <h5>
          Teaching
        </h5>
        <CryptoTeaching
          v-for="(teaching, index) in teachings"
          :key="index"
          v-bind="teaching"
        ></CryptoTeaching>

        <h5>
          Organization
        </h5>

        <h5>
          Tools
        </h5>
      </div>
    </div>
  </q-page>
</template>

<script>
import CryptoPublication from 'components/CryptoPublication.vue'
import CryptoTeaching from 'components/CryptoTeaching.vue'
import publications from './../data/crypto-publications.json'
import teachings from './../data/crypto-teachings.json'

export default {
  name: 'PageCrypto',
  components: { CryptoPublication, CryptoTeaching },
  data () {
    return {
      publications,
      teachings
    }
  }
}
</script>
