<template>
  <div class="about">
    <img src="@/assets/banner.png" id="banner" />
    <div class="cards">
      <div></div>
      <div class="card">
        <img src="../assets/santi.jpeg" alt="santi" />
        <div>
          <h4>Santiago Andres Gordillo Piñeros</h4>
          <p>Frontend Developer</p>
        </div>
      </div>
      <div class="card">
        <img src="../assets/gina.jpeg" alt="gina" />
        <div>
          <h4>Gina Marcela Diaz Pinzón</h4>
          <p>Backend Developer</p>
        </div>
      </div>

      <div class="card">
        <img src="../assets/lina.jpeg" alt="lina" />
        <div>
          <h4>Lina Marcela Rodríguez Pérez</h4>
          <p>Product Owner</p>
        </div>
      </div>
      <div class="card">
        <img src="../assets/henry.jpg" alt="henry" />
        <div>
          <h4>Henry Cabarcas Ortiz</h4>
          <p>Scrum Master</p>
        </div>
      </div>
      <div class="card">
        <img src="../assets/nat.jpeg" alt="nat" />
        <div>
          <h4>Natalia Narváez Rodríguez</h4>
          <p>Database Analyst</p>
        </div>
      </div>
      <div></div>
    </div>
  </div>
</template>

<script>
export default {
  name: "About",
  data() {
    return {
      names: ["nat.jpeg", "santi.jpeg", "gina.jpeg", "lina.jpeg", "henry.jpg"],
    };
  },
};
</script>

<style lang="scss">
.about {
  padding: 1rem 1.25rem;
  overflow: visible;
}
.cards {
  column-count: 3;
  overflow: visible;
  flex-wrap: wrap;
  padding-top: 1rem;
  div {
    display: inline-table;
    margin: 1rem;
  }
}
.card {
  display: block;
  overflow: hidden;
  background-color: white;
  width: 30%;
  img {
    display: block;
    width: 300px;
    margin: 0;
  }
  div {
    padding: 1rem 0.5rem;
    display: block;
    text-align: left;
  }
  p {
    margin-top: 0.5rem;
    display: block;
    text-align: left;
  }
}
.card:hover {
  box-shadow: 0px 0px 12px 2px rgba(0, 0, 0, 0.555);
  animation: zoom 200ms ease-in-out;
  transform: scale(1.15, 1.15);
}
@keyframes zoom {
  0% {
    transform: scale(1, 1);
  }
  100% {
    transform: scale(1.15, 1.15);
  }
}
</style>
