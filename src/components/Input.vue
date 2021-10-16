<template>
  <div>
    <label class="x">{{ title }}</label>
    <input
      type="{{type}}"
      name="{{title}}"
      :value="value"
      @input="$emit('update:value', $event.target.value)"
    />
  </div>
</template>

<script>
export default {
  name: "Input",
  props: {
    title: String,
    value: String,
    type: String
  }
}
</script>

<style lang="css" scoped>
div {
  display: block;
  align-items: center;
  margin: 8px;
}
label {
  display: block;
}
input {
  display: block;
  width: 100%;
  height: 1.25em;
  border-radius: 0;
  border: 1px grey solid;
  box-shadow: 0px 2px 2px 1px rgba(0, 80, 133, 0.5);
}
</style>