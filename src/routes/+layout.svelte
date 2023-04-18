<script lang="ts">
    import type { PageData } from './$types'
    import Icon from '@iconify/svelte';
    import "../app.css";
    import Header from "$lib/Header.svelte";
    import Footer from "$lib/Footer.svelte";

    export let data: PageData;
</script>
  
<div class="mx-2 md:mx-auto max-w-3xl md:max-w-5xl lg:max-w-7xl my-5 md:my-8 lg:my-10">
    <div class="container mx-auto">
        <Header user={data.user} />
            <div class="my-10 md:my-12 lg:mx-24">
                <slot />
            </div>
        <Footer/>
    </div>
</div>
