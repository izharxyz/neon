<script lang="ts">
    import type { PageData } from "./$types";
    export let data: PageData
    $: ({ posts } = data)
</script>


<div class="flex flex-row justify-between">
    <div class="w-1/3 p-8 m-20 bg-gray-200 rounded-md border-2 border-gray-400">
        {#each posts as post}
            <h3>
                {post.title}
            </h3>
            <p>
                {post.content}
            </p>
        {/each}
    </div>
    
    <div class="w-1/3 p-8 m-20 bg-gray-200 rounded-md border-2 border-gray-400">
        <form action="?/createPost" method="POST" class="flex flex-col">
            <h3 class=""> Create new Post </h3>
            <label for="title" class="mt-2 py-2"> Title </label>
            <input type="text" name="title" id="title" class="rounded-md p-2">
            <label for="content" class="mt-2 py-2"> Content </label>
            <textarea name="content" id="contnet" cols="30" rows="10" class="rounded-md p-2"></textarea>
            <button type="submit" class="w-full bg-gray-300 border-2 border-gray-400 rounded-md mt-2 p-2"> Create </button>
        </form>
    </div>
</div>
