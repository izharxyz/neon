<script lang="ts">
    import type { PageData } from "./$types";
    export let data: PageData
    $: ({ posts } = data)
</script>


<div class="grid grid-cols-2 mx-auto">
    <div class="col-span-1 p-8 m-20 bg-gray-200 rounded-md border-2 border-gray-400">
        {#each posts as post} 
            <h3 class="bg-gray-300 p-2 mt-2 w-full rounded-t-md">
                {post.title}
            </h3>
            <p class="border-2 border-gray-300 p-2 w-full rounded-b-md">
                {post.content}
            </p>
            <form action="?/deletePost&id={post.id}" method="POST" class="py-2 flex-row">
                <button type="submit" class="px-3 py-1 bg-red-400 text-white rounded">Delete</button>
                <button class="px-3 py-1 bg-blue-400 text-white rounded"><a href="/{post.id}">Update</a></button>
            </form>
        {/each}
    </div>
    <div>
        <div class="p-8 m-20 bg-gray-200 rounded-md border-2 border-gray-400 sticky top-8">
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
</div>