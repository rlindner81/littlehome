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

        <h5>
          Teaching
        </h5>

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
    name: "Monoidic Codes in Cryptography",
    link: "http://eprint.iacr.org/2011/371",
    authors: [
      { name: "Paulo S. L. M. Barreto", link: "http://www.larc.usp.br/~pbarreto/" },
      { name: "Richard Lindner" },
      { name: "Rafael Misoczki", link: "http://www.larc.usp.br/~rmisoczki/" }
    ],
    archive: { name: "Cryptology ePrint Archive", link: "http://eprint.iacr.org/" },
    details: "Technical Report 2011/371, 2011"
  },
  {
    name: "Curriculum Vitae (German)",
    link: "crypto/cv-rlindner-jul2011.pdf",
    variants: [
      { name: "tex", link: "crypto/cv.zip" }
    ],
    authors: [
      { name: "Richard Lindner" }
    ],
    details: "July 2011"
  },
  {
    name: "Towards Efficient Lattice-Based Cryptography",
    link: "http://tuprints.ulb.tu-darmstadt.de/2387/",
    variants: [
      { name: "slides", link: "crypto/defense.pptx" },
      { name: "tex", link: "crypto/diss.zip" }
    ],
    authors: [
      { name: "Richard Lindner" }
    ],
    details: "PhD Thesis, Technische Universität Darmstadt, 2011"
  },
  {
    name: "Better Key Sizes (and Attacks) for LWE-Based Encryption",
    link: "crypto/lwe-analysis.pdf",
    variants: [
      { name: "slides", link: "crypto/lwe-analysis.pptx" }
    ],
    authors: [
      { name: "Richard Lindner" },
      { name: "Chris Peikert", link: "http://www.cc.gatech.edu/~cpeikert/" }
    ],
    archive: { name: "CT-RSA 2011", link: "http://ct-rsa2011.di.uoa.gr/" },
    details: "Lecture Notes in Computer Science, Volume 6558, pp. 319-339, Springer, 2011"
  },
  {
    name: "Decoding Square-Free Goppa Codes over F_p",
    link: "http://eprint.iacr.org/2010/372",
    variants: [
      { name: "slides", link: "crypto/goppadec-slides.pdf" }
    ],
    authors: [
      { name: "Paulo S. L. M. Barreto", link: "http://www.larc.usp.br/~pbarreto/" },
      { name: "Richard Lindner" },
      { name: "Rafael Misoczki", link: "http://www.larc.usp.br/~rmisoczki/" }
    ],
    archive: { name: "Cryptology ePrint Archive", link: "http://eprint.iacr.org/" },
    details: "Technical Report 2010/372, 2010"
  },
  {
    name: "Improved Zero-Knowledge Identification with Lattices",
    link: "crypto/LatticeIdent.pdf",
    variants: [
      { name: "slides", link: "crypto/identification.pptx" }
    ],
    authors: [
      { name: "Pierre-Louis Cayrel", link: "http://cayrel.net/" },
      { name: "Richard Lindner" },
      { name: "Markus Rückert", link: "http://www.cdc.informatik.tu-darmstadt.de/mitarbeiter/rueckert.html" },
      { name: "Rosemberg Silva" },
    ],
    archive: { name: "ProvSec 2010", link: "http://fist.mmu.edu.my/provsec2010/" },
    details: "Lecture Notes in Computer Science, Volume 6402, pp. 1-17, Springer, 2010"
  },
  {
    name: "An Efficient Lattice-Based Threshold Ring Signature Scheme",
    link: "crypto/LatticeRingSignature.pdf",
    variants: [
      { name: "slides", link: "crypto/LatticeRingSignature-slides.pdf" }
    ],
    authors: [
      { name: "Pierre-Louis Cayrel", link: "http://cayrel.net/" },
      { name: "Richard Lindner" },
      { name: "Markus Rückert", link: "http://www.cdc.informatik.tu-darmstadt.de/mitarbeiter/rueckert.html" },
      { name: "Rosemberg Silva" },
    ],
    archive: { name: "Latincrypt 2010", link: "http://cti.cs.buap.mx/latin/index.php" },
    details: "Lecture Notes in Computer Science, Volume 6212, pp. 255-272, Springer, 2010"
  },
  {
    name: "Density of Ideal Lattices",
    link: "crypto/density.pdf",
    variants: [
      { name: "slides", link: "crypto/density.ppt" }
    ],
    authors: [
      { name: "Johannes Buchmann", link: "https://www.cdc.informatik.tu-darmstadt.de/de/cdc/personen/johannes-buchmann/" },
      { name: "Richard Lindner" },
    ],
    archive: { name: "WEWoRC 2009", link: "http://2009.weworc.org/" },
    details: "Lecture Notes in Computer Science, Volume 6429, pp. xx-xx, Springer, 2010"
  },
  {
    name: "Probabilistic Analysis of LLL Reduced Bases",
    link: "crypto/problll.pdf",
    authors: [
      { name: "Michael Schneider", link: "http://www.cdc.informatik.tu-darmstadt.de/mitarbeiter/mischnei.html" },
      { name: "Johannes Buchmann", link: "https://www.cdc.informatik.tu-darmstadt.de/de/cdc/personen/johannes-buchmann/" },
      { name: "Richard Lindner" },
    ],
    archive: { name: "WEWoRC 2009", link: "http://2009.weworc.org/" },
    details: "Lecture Notes in Computer Science, Volume 6429, pp. xx-xx, Springer, 2010"
  },
  {
    name: "Secure Parameters for SWIFFT",
    link: "crypto/swifft.pdf",
    variants: [
      { name: "slides", link: "crypto/swifft.ppt" }
    ],
    authors: [
      { name: "Johannes Buchmann", link: "https://www.cdc.informatik.tu-darmstadt.de/de/cdc/personen/johannes-buchmann/" },
      { name: "Richard Lindner" },
    ],
    archive: { name: "Indocrypt 2009", link: "http://indocrypt09.inria.fr/" },
    details: "Lecture Notes in Computer Science, Volume 5922, pp. 1-17, Springer, 2009"
  },
  {
    name: "Post-Quantum Cryptography: Lattice Signatures",
    link: "http://www.springerlink.com/content/g81383607j400n68/",
    variants: [
      { name: "slides", link: "crypto/signatures.ppt" }
    ],
    authors: [
      { name: "Johannes Buchmann", link: "https://www.cdc.informatik.tu-darmstadt.de/de/cdc/personen/johannes-buchmann/" },
      { name: "Richard Lindner" },
      { name: "Markus Rückert", link: "http://www.cdc.informatik.tu-darmstadt.de/mitarbeiter/rueckert.html" },
      { name: "Michael Schneider", link: "http://www.cdc.informatik.tu-darmstadt.de/mitarbeiter/mischnei.html" },
    ],
    archive: { name: "CECC 2008", link: "http://www.math.tugraz.at/~cecc08/" },
    details: "Special Issue of Computing, Springer, 2009"
  },
  {
    name: "Explicit Hard Instances of the Shortest Vector Problem",
    link: "crypto/challenge.pdf",
    variants: [
      { name: "slides", link: "crypto/challenge.ppt" },
      { name: "latticechallenge", link: "http://www.latticechallenge.org/" }
    ],
    authors: [
      { name: "Johannes Buchmann", link: "https://www.cdc.informatik.tu-darmstadt.de/de/cdc/personen/johannes-buchmann/" },
      { name: "Richard Lindner" },
      { name: "Markus Rückert", link: "http://www.cdc.informatik.tu-darmstadt.de/mitarbeiter/rueckert.html" },
      { name: "Michael Schneider", link: "http://www.cdc.informatik.tu-darmstadt.de/mitarbeiter/mischnei.html" },
    ],
    archive: { name: "PQCrypto 2008", link: "http://math.uc.edu/~aac/pqcrypto2008/" },
    details: "Lecture Notes in Computer Science, Volume 5299, pp. 79-94, Springer, 2008"
  },
  {
    name: "Efficiency Improvement for NTRU",
    link: "crypto/ntrusves.pdf",
    variants: [
      { name: "slides", link: "crypto/ntrusves.ppt" },
    ],
    authors: [
      { name: "Johannes Buchmann", link: "https://www.cdc.informatik.tu-darmstadt.de/de/cdc/personen/johannes-buchmann/" },
      { name: "Richard Lindner" },
      { name: "Martin Döring", link: "http://www.cdc.informatik.tu-darmstadt.de/mitarbeiter/doering.html" },
    ],
    archive: { name: "Sicherheit 2008", link: "http://www.sicherheit2008.de/" },
    details: "Lecture Notes in Informatics, Volume 128, pp. 163-178, Gesellschaft für Informatik, 2008"
  },
  {
    name: "Identifying Ideal Lattices",
    link: "http://eprint.iacr.org/2007/322",
    authors: [
      { name: "Jintai Ding", link: "http://math.uc.edu/~ding/" },
      { name: "Richard Lindner" },
    ],
    archive: { name: "Cryptology ePrint Archive", link: "http://eprint.iacr.org/" },
    details: "Technical Report 2007/322, 2007"
  },
  {
    name: "Current Attacks on NTRU",
    link: "http://www.cdc.informatik.tu-darmstadt.de/reports/reports/Richard_Lindner.ntru.diplom.pdf",
    variants: [
      { name: "book", link: "http://www.amazon.de/dp/363904780X/" },
    ],
    authors: [
      { name: "Richard Lindner" },
    ],
    details: "Diploma Thesis, Technische Universität Darmstadt, 2006"
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
