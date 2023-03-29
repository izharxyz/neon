<script>
    import Editor from '$lib/Editor.svelte'
</script>
  
<div>
    <form action="?/createPost">
        <Editor />
        <button type="submit" class="btn btn-primary btn-sm mt-4"> Submit </button>
    </form> 
</div>