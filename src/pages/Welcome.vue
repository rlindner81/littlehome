<template>
  <q-page class="flex-block">
    <div class="row q-pa-md q-col-gutter-md">
      <div class="col-12">
        <h4>
          Welcome
        </h4>
      </div>

      <div class="col-4">
        <q-img
          src="welcome/rlindner.jpg"></q-img>
      </div>
      <div class="col-8">
        <h5>
        Dr. Richard Lindner
        </h5>
        <a
          target="_blank" href="https://sap.com">
          SAP SE
        </a><br/>
        Dietmar-Hopp-Allee 16<br/>
        69190 Walldorf<br/>
        Germany<br/>
        <br/>
        <a
          href="mailto:rlindner@gmail.com">
          rlindner81@gmail.com
        </a>
      </div>

      <div class="col-4">
        <router-link
          to="/crypto">
          <q-img
            fit="none"
            position="50% 0"
            src="welcome/crypto.png"></q-img>
        </router-link>
      </div>
      <div class="col-4">
        <router-link
          to="/math">
          <q-img
            fit="none"
            position="50% 0"
            src="welcome/math.png"></q-img>
        </router-link>
      </div>
      <div class="col-4">
        <router-link
          to="/theater">
          <q-img
            fit="none"
            position="50% 0"
            src="welcome/theater.png"></q-img>
        </router-link>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'PageWelcome'
}
</script>
