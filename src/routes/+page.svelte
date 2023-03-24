<script lang="ts">
    import type { PageData } from "./$types";
    import HeroCard from "$lib/post/HeroCard.svelte";
    import PostCard from "$lib/post/PostCard.svelte";
    import Categories from "$lib/sidebar/Categories.svelte";
    import Popular from "$lib/sidebar/Popular.svelte";
    import Carousel from "$lib/post/Carousel.svelte";

    export let data: PageData
    $: ({ posts } = data)

    const arr: number[]= [1,1,1,1,1,1,1,1,1,1];
</script>

<div class="grid grid-cols-1 md:grid-cols-11 gap-6">
    <div class="col-span-1 md:col-span-11">
        <h1 class="mb-2 text-bold text-md text-primary">Trending posts</h1>
        <Carousel/>
    </div>
    <div class="col-span-1 md:col-span-8">
        <HeroCard/>
        <div class="col-span-1 md:col-span-8">
            {#each arr as arr}
                <PostCard/>
            {/each}
        </div>
    </div>
    <div class="col-span-1 md:col-span-3 w-full">
        <Categories/>
        <Popular/>
    </div>
</div>