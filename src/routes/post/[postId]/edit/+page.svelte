<script lang="ts">
	import { enhance } from '$app/forms';
    import Editor from '$lib/components/Editor.svelte'
    import type { PageData } from "./$types";

    export let data: PageData
    $: ({ post } = data)

    let content: any;

    // @ts-ignore
    const getHtmlOutput = ({ detail }) => {
        content = detail;
    }
</script>
  
<div class="card border border-primary-content p-2">
    <h1 class="my-8">
        Write a wonderful article
    </h1>
    <form method="POST" use:enhance>
        <input name="title" type="text" placeholder="Title" class="input input-bordered input-primary w-full" value="{post.title}"/>
        <input name="excerpt" type="text" placeholder="Excerpt" class="input input-bordered input-primary w-full mt-8" value="{post.excerpt}"/>

        <div class="flex flex-col md:flex-row my-8">
            <select name="category" required class="select select-primary w-full md:w-1/2 md:mr-5">
                <option disabled selected>Category</option>
                <option>Web dev</option>
                <option>Mobile dev</option>
                <option>Blockchain</option>
                <option>Artificial intelligence</option>
            </select>
            <input name="thumbnail" type="file" class="file-input file-input-bordered file-input-primary w-full md:w-1/2 mt-8 md:mt-0" />
        </div>
        <div>
            <input type="hidden" name="content" value={content}>
        </div>
        <div class="p-2 border border-primary card">
            <Editor on:html-change={getHtmlOutput} content={post.content}/>
        </div>
        <button type="submit" class="btn btn-primary mt-8"> Update </button>
    </form> 
</div>