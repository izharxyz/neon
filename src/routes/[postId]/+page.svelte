<script lang="ts">
    import type { PageData } from "./$types";
    export let data: PageData
    $: ({ post } = data)
</script>

<div class="p-8 m-20 bg-gray-200 rounded-md border-2 border-gray-400 sticky top-8">
    <form action="?/updatePost" method="POST" class="flex flex-col">
        <h3 class=""> Update {post.title} </h3>
        <label for="title" class="mt-2 py-2"> Title </label>
        <input type="text" name="title" id="title" class="rounded-md p-2" value="{post.title}">
        <label for="content" class="mt-2 py-2"> Content </label>
        <textarea name="content" id="contnet" cols="30" rows="10" class="rounded-md p-2" value="{post.content}"></textarea>
        <button type="submit" class="w-full bg-gray-300 border-2 border-gray-400 rounded-md mt-2 p-2"> Update </button>
    </form>
</div>