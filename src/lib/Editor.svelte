<script lang="ts">
  import StarterKit from "@tiptap/starter-kit";
  import { Editor } from "@tiptap/core";
  import { onMount } from "svelte";

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
        bold
      </button>
      <button
        on:click={() => editor.chain().focus().toggleItalic().run()}
        disabled={!editor.can().chain().focus().toggleItalic().run()}
        class={editor.isActive("italic") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        italic
      </button>
      <button
        on:click={() => editor.chain().focus().toggleStrike().run()}
        disabled={!editor.can().chain().focus().toggleStrike().run()}
        class={editor.isActive("strike") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        strike
      </button>
      <button
        on:click={() => editor.chain().focus().toggleCode().run()}
        disabled={!editor.can().chain().focus().toggleCode().run()}
        class={editor.isActive("code") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        code
      </button>
      <button on:click={() => editor.chain().focus().unsetAllMarks().run()}> clear marks </button>
      <button on:click={() => editor.chain().focus().clearNodes().run()}> clear nodes </button>
      <button
        on:click={() => editor.chain().focus().setParagraph().run()}
        class={editor.isActive("paragraph") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        paragraph
      </button>
      <button
        on:click={() => editor.chain().focus().toggleHeading({ level: 1 }).run()}
        class={editor.isActive("heading", { level: 1 }) ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        h1
      </button>
      <button
        on:click={() => editor.chain().focus().toggleHeading({ level: 2 }).run()}
        class={editor.isActive("heading", { level: 2 }) ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        h2
      </button>
      <button
        on:click={() => editor.chain().focus().toggleHeading({ level: 3 }).run()}
        class={editor.isActive("heading", { level: 3 }) ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        h3
      </button>
      <button
        on:click={() => editor.chain().focus().toggleHeading({ level: 4 }).run()}
        class={editor.isActive("heading", { level: 4 }) ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        h4
      </button>
      <button
        on:click={() => editor.chain().focus().toggleHeading({ level: 5 }).run()}
        class={editor.isActive("heading", { level: 5 }) ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        h5
      </button>
      <button
        on:click={() => editor.chain().focus().toggleHeading({ level: 6 }).run()}
        class={editor.isActive("heading", { level: 6 }) ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        h6
      </button>
      <button
        on:click={() => editor.chain().focus().toggleBulletList().run()}
        class={editor.isActive("bulletList") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        bullet list
      </button>
      <button
        on:click={() => editor.chain().focus().toggleOrderedList().run()}
        class={editor.isActive("orderedList") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        ordered list
      </button>
      <button
        on:click={() => editor.chain().focus().toggleCodeBlock().run()}
        class={editor.isActive("codeBlock") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        code block
      </button>
      <button
        on:click={() => editor.chain().focus().toggleBlockquote().run()}
        class={editor.isActive("blockquote") ? "btn btn-xs btn-accent" : "btn btn-xs"}
      >
        blockquote
      </button>
      <button on:click={() => editor.chain().focus().setHorizontalRule().run()}>
        horizontal rule
      </button>
      <button on:click={() => editor.chain().focus().setHardBreak().run()}> hard break </button>
      <button
        on:click={() => editor.chain().focus().undo().run()}
        disabled={!editor.can().chain().focus().undo().run()}
      >
        undo
      </button>
      <button
        on:click={() => editor.chain().focus().redo().run()}
        disabled={!editor.can().chain().focus().redo().run()}
      >
        redo
      </button>
    </div>
  </div>
{/if}
<div bind:this={element} />
