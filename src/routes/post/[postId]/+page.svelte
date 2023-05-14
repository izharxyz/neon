<script lang="ts">
	import { page } from '$app/stores';
	import type { PageData } from './$types';
	export let data: PageData;
	$: ({ post } = data);
</script>

<div>
	<h1 class="my-8 text-primary">{post.title}</h1>
	<h3 class="mb-8">{post.excerpt}</h3>
	<div class="w-full">
		{@html post.content}
	</div>
	<a href="{$page.url}/edit/"><button class="my-8 btn btn-accent">Edit</button></a>
</div>
