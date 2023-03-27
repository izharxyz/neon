<script lang="ts">
    import type { PageData } from "./$types";
    export let data: PageData
    $: ({ search } = data)
</script>

<h1 class="text-4xl text-primary"> Your search is: <span class="text-info">{search}</span> </h1>