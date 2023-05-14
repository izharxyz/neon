<script lang="ts">
	import type { PageData } from './$types';
	import HeroCard from '$lib/components/post/HeroCard.svelte';
	import PostCard from '$lib/components/post/PostCard.svelte';
	import Categories from '$lib/components/sidebar/Categories.svelte';
	import Popular from '$lib/components/sidebar/Popular.svelte';
	import Carousel from '$lib/components/post/Carousel.svelte';

	export let data: PageData;
	$: ({ posts } = data);
</script>

<div class="grid grid-cols-1 md:grid-cols-11 gap-6">
	<div class="col-span-1 md:col-span-11">
		<h1 class="mb-2 text-bold text-xl text-md text-primary">Trending posts</h1>
		<Carousel />
	</div>
	<div class="col-span-1 md:col-span-8">
		<HeroCard title={posts[0].title} excerpt={posts[0].excerpt} postId={posts[0].id} />
		<div class="col-span-1 md:col-span-8">
			{#each posts as post}
				<PostCard title={post.title} excerpt={post.excerpt} postId={post.id} />
			{/each}
		</div>
	</div>
	<div class="col-span-1 md:col-span-3 w-full">
		<Categories />
		<Popular />
	</div>
</div>
