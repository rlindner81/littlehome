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
          v-for="publication in publications"
          :key="publication.name"
          v-bind="publication"
        ></CryptoPublication>
      </div>
    </div>
  </q-page>
</template>

<script>
import CryptoPublication from 'components/CryptoPublication.vue'

const publications = [
  {
    name: "A Lattice-Based Batch Identification Scheme",
    link: "crypto/batchid.pdf",
    authors: [
      { name: "Rosemberg Silva" },
      { name: "Pierre-Louis Cayrel", link: "http://cayrel.net/" },
      { name: "Richard Lindner" }
    ],
    archive: { name: "ITW 2011", link: "http://www.fee.unicamp.br/itw2011/" },
    details: "IEEE, 2011"
  },
  {
    name: "name2",
    link: "link2",
    variants: [{ name: "tex", link: "texLink" }, { name: "slides", link: "slideLink" }],
    authors: [{ name: "Richard Lindner", link: "namelink" }]
  },
  {
    name: "name3",
    link: "link3",
    authors: [{ name: "Richard Lindner" }, { name: "JAAJ", link:"ajjalink" }]
  }
];

export default {
  name: 'PageCrypto',
  components: { CryptoPublication },
  data () {
    return {
      publications
    }
  }
}
</script>
