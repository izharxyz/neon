<script lang="ts">
  import StarterKit from "@tiptap/starter-kit";
  import { Editor } from "@tiptap/core";
  import { onMount } from "svelte";


  import MdFormatBold from 'svelte-icons/md/MdFormatBold.svelte'
  import MdFormatItalic from 'svelte-icons/md/MdFormatItalic.svelte'
  import MdStrikethroughS from 'svelte-icons/md/MdStrikethroughS.svelte'
  import MdCode from 'svelte-icons/md/MdCode.svelte'
  import MdClear from 'svelte-icons/md/MdClear.svelte'
  import MdBackspace from 'svelte-icons/md/MdBackspace.svelte'
  import MdLocalParking from 'svelte-icons/md/MdLocalParking.svelte'
  import MdFormatListBulleted from 'svelte-icons/md/MdFormatListBulleted.svelte'
  import MdReorder from 'svelte-icons/md/MdReorder.svelte'
  import MdFormatQuote from 'svelte-icons/md/MdFormatQuote.svelte'
  import MdBorderHorizontal from 'svelte-icons/md/MdBorderHorizontal.svelte'
  import MdUndo from 'svelte-icons/md/MdUndo.svelte'
  import MdRedo from 'svelte-icons/md/MdRedo.svelte'

  import FaUndoAlt from 'svelte-icons/fa/FaUndoAlt.svelte'
  import FaRedoAlt from 'svelte-icons/fa/FaRedoAlt.svelte'


  let element: any;
  let editor: any;

  onMount(() => {
    editor = new Editor({
      element: element,
      editorProps: {
        attributes: {
          class: 'p-2 mt-2 border border-primary card',
        },
      },
      extensions: [StarterKit],
      content: `
          <input name="content" id="content" placeholder="content">
          `,
      onTransaction: () => {
        // force re-render so `editor.isActive` works as expected
        editor = editor;
      },
    });
  });
</script>

{#if editor}
  <div class="border border-primary p-10 card">
    <div>
      <button
        on:click={() => editor.chain().focus().toggleBold().run()}
        disabled={!editor.can().chain().focus().toggleBold().run()}
        class={editor.isActive("bold") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        <div class="h-6 w-6">
          <MdFormatBold/>
        </div>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleItalic().run()}
        disabled={!editor.can().chain().focus().toggleItalic().run()}
        class={editor.isActive("italic") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        <div class="h-6 w-6">
          <MdFormatItalic/>
        </div>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleStrike().run()}
        disabled={!editor.can().chain().focus().toggleStrike().run()}
        class={editor.isActive("strike") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        <div class="h-6 w-6">
          <MdStrikethroughS/>
        </div>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleCode().run()}
        disabled={!editor.can().chain().focus().toggleCode().run()}
        class={editor.isActive("code") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        <div class="h-6 w-6">
          <MdCode/>
        </div>
      </button>
      <button on:click={() => editor.chain().focus().unsetAllMarks().run()}>  
        <div class="h-6 w-6">
          <MdBackspace/>
        </div> 
      </button>
      <button on:click={() => editor.chain().focus().clearNodes().run()}> 
        <div class="h-6 w-6">
          <MdClear/>
        </div> 
      </button>
      <button
        on:click={() => editor.chain().focus().setParagraph().run()}
        class={editor.isActive("paragraph") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        <div class="h-6 w-6">
          <MdLocalParking/>
        </div> 
      </button>
      
      <button
        on:click={() => editor.chain().focus().toggleBulletList().run()}
        class={editor.isActive("bulletList") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        <div class="h-6 w-6">
          <MdFormatListBulleted/>
        </div>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleOrderedList().run()}
        class={editor.isActive("orderedList") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        <div class="h-6 w-6">
          <MdReorder/>
        </div>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleCodeBlock().run()}
        class={editor.isActive("codeBlock") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        <div class="h-6 w-6">
          <MdCode/>
        </div>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleBlockquote().run()}
        class={editor.isActive("blockquote") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        <div class="h-6 w-6">
          <MdFormatQuote/>
        </div>
      </button>
      
      <button
        on:click={() => editor.chain().focus().undo().run()}
        disabled={!editor.can().chain().focus().undo().run()}
      >
        <div class="h-5 w-5">
          <FaUndoAlt/>
        </div>
      </button>
      <button
        on:click={() => editor.chain().focus().redo().run()}
        disabled={!editor.can().chain().focus().redo().run()}
      >
        <div class="h-5 w-5">
          <FaRedoAlt/>
        </div>
      </button>
    </div>
  </div>
{/if}
<div bind:this={element} />
