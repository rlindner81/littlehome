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
        Cryptographic primitives and protocols resistant to quantum computer
        attacks. In particular, practical and provably secure schemes with weak
        hardness assumptions.

        <h5>
          Publications
        </h5>
        <CryptoPublication
          v-for="(publication, index) in publications"
          :key="'publication' + index"
          v-bind="publication"
        ></CryptoPublication>

        <h5>
          Teaching
        </h5>
        <CryptoTeaching
          v-for="(teaching, index) in teachings"
          :key="'teaching' + index"
          v-bind="teaching"
        ></CryptoTeaching>

        <h5>
          Organization
        </h5>
        <p>
          Supervision of Bachelor-, Master-, and Diploma Theses
        </p>
        <p>
          Group seminar -
          <a
            href="https://www.cdc.informatik.tu-darmstadt.de/de/studium-und-lehre/lehrveranstaltungen/oberseminar/"
          >
            Oberseminar
          </a>
          - 2007 (<a
            href="http://www.cdc.informatik.tu-darmstadt.de/lehre/WS07_08/seminar/OS.html"
            >Winter</a
          >), 2008 (<a
            href="http://www.cdc.informatik.tu-darmstadt.de/lehre/SS08/seminar/OS.html"
            >Summer</a
          >/<a
            href="http://www.cdc.informatik.tu-darmstadt.de/lehre/WS08_09/seminar/OS.html"
            >Winter</a
          >), 2009 (<a
            href="http://www.cdc.informatik.tu-darmstadt.de/lehre/SS09/seminar/OS.html"
            >Summer</a
          >/<a
            href="http://www.cdc.informatik.tu-darmstadt.de/lehre/WS09_10/seminar/OS.html"
            >Winter</a
          >), 2010 (<a
            href="http://www.cdc.informatik.tu-darmstadt.de/lehre/SS10/seminar/OS.html"
            >Summer</a
          >/<a
            href="http://www.cdc.informatik.tu-darmstadt.de/lehre/WS10_11/seminar/OS.html"
            >Winter</a
          >), 2011 (<a
            href="https://www.cdc.informatik.tu-darmstadt.de/?id=4647"
            >Summer</a
          >)
        </p>
        <p>
          Crypto Lab - 2010 (<a
            href="http://www.cdc.informatik.tu-darmstadt.de/lehre/SS10/praktikum/Kryptographie-Praktikum.html"
            >Summer</a
          >/<a
            href="http://www.cdc.informatik.tu-darmstadt.de/lehre/WS10_11/praktikum/Kryptographie-Praktikum.html"
            >Winter</a
          >), 2011 (<a
            href="https://www.cdc.informatik.tu-darmstadt.de/?id=4647"
            >Summer</a
          >)
        </p>
        <p>
          <a href="http://www.cased.de/news/veranstaltungen/tgit09.html"
            >2nd Taiwan-Germany Information Technology Workshop (TGIT 2009)</a
          >
        </p>

        <h5>
          Tools
        </h5>
        <table>
          <tbody>
            <tr>
              <td width="80" style="vertical-align:top">
                9.8.2010
              </td>
              <td>
                <p>
                  <a
                    href="https://doc.sagemath.org/html/en/reference/cryptography/sage/crypto/lattice.html"
                  >
                    <b>sage.crypto.gen_lattice()</b><br />
                  </a>
                  Richard Lindner and
                  <a
                    href="http://www.cdc.informatik.tu-darmstadt.de/mitarbeiter/mischnei.html"
                    >Michael Schneider</a
                  ><br />This generator produces
                  <span style="font-style:italic">modular</span>,
                  <span style="font-style:italic">random</span>,
                  <span style="font-style:italic">ideal</span>, and
                  <span style="font-style:italic">cyclotomic</span> lattice
                  bases and their scaled duals in SAGE and NTL/fpLLL readable
                  format. It is part of
                  <a href="http://www.sagemath.org/">SAGE</a>
                  4.5.2 and above
                </p>
              </td>
            </tr>
            <tr>
              <td style="vertical-align:top">
                23.5.2009
              </td>
              <td>
                <p>
                  <b><a href="crypto/ziplatex.py">ziplatex.py</a></b>
                  <br />for packaging document sources (copy into tex-dir and
                  run)
                </p>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </q-page>
</template>

<script>
import CryptoPublication from "components/CryptoPublication.vue";
import CryptoTeaching from "components/CryptoTeaching.vue";
import publications from "./../data/crypto-publications.json";
import teachings from "./../data/crypto-teachings.json";

export default {
  name: "PageCrypto",
  components: { CryptoPublication, CryptoTeaching },
  data() {
    return {
      publications,
      teachings
    };
  }
};
</script>
