<script lang="ts">
  import StarterKit from "@tiptap/starter-kit";
  import { lowlight } from 'lowlight/lib/core';

  import Image from '@tiptap/extension-image';
  
  import Document from '@tiptap/extension-document';
  import Paragraph from '@tiptap/extension-paragraph';
  import Heading from '@tiptap/extension-heading';
  import Blockquote from '@tiptap/extension-blockquote';
  import CodeBlockLowlight from '@tiptap/extension-code-block-lowlight';

  import Code from '@tiptap/extension-code';

  import { Editor } from "@tiptap/core";
  import { onMount } from "svelte";
	import Icon from "@iconify/svelte";

  let element: any;
  let editor: any;

  onMount(() => {
    editor = new Editor({
      element: element,
      editorProps: {
        attributes: {
          class: 'textarea textarea-bordered textarea-lg p-5 mt-2',
        },
      },
      extensions: [
        StarterKit,

        Paragraph.configure({
        HTMLAttributes: {
          class: '',
        },
        }),

        Heading.configure({
          HTMLAttributes: {
            class: '',
          },
        }),

        Blockquote.configure({
          HTMLAttributes: {
            class: 'card w-full grid place-items-center p-5 md:p-10 bg-primary-content text-neutral-content',
          },
        }),

        CodeBlockLowlight.configure({
          lowlight,
          defaultLanguage: 'js',
          languageClassPrefix: 'language-',
          HTMLAttributes: {
            class: 'w-full border border-primary-content p-2 rounded-md bg-base-300',
          },
        }),

        Code.configure({
          HTMLAttributes: {
            class: 'border border-primary-content px-1 rounded-md bg-base-300',
            },
        }),


      ],
      content: ``,
      onTransaction: () => {
        // force re-render so `editor.isActive` works as expected
        editor = editor;
      },
    });

    const html = editor.getHTML()
    
  });
</script>

{#if editor}
  <div class="border p-2 md:p-8 border-primary-content card">
    <div class="mx-auto">
      <button
        on:click={() => editor.chain().focus().toggleBold().run()}
        disabled={!editor.can().chain().focus().toggleBold().run()}
        class={editor.isActive("bold") ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="material-symbols:format-bold" class="editor-icon"/>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleItalic().run()}
        disabled={!editor.can().chain().focus().toggleItalic().run()}
        class={editor.isActive("italic") ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="material-symbols:format-italic" class="editor-icon"/>
      </button>
      
      <button
        on:click={() => editor.chain().focus().toggleStrike().run()}
        disabled={!editor.can().chain().focus().toggleStrike().run()}
        class={editor.isActive("strike") ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="material-symbols:format-strikethrough" class="editor-icon"/>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleCode().run()}
        disabled={!editor.can().chain().focus().toggleCode().run()}
        class={editor.isActive("code") ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="material-symbols:code" class="editor-icon"/>
      </button>
      <button on:click={() => editor.chain().focus().unsetAllMarks().run()} class="btn btn-xs"> <Icon icon="material-symbols:format-clear" class="editor-icon"/> </button>
      <button on:click={() => editor.chain().focus().clearNodes().run()} class="btn btn-xs"> <Icon icon="ic:baseline-clear" class="editor-icon"/> </button>
      <button
        on:click={() => editor.chain().focus().setParagraph().run()}
        class={editor.isActive("paragraph") ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="material-symbols:format-paragraph" class="editor-icon"/>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleHeading({ level: 1 }).run()}
        class={editor.isActive("heading", { level: 1 }) ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="material-symbols:format-h1" class="editor-icon"/>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleHeading({ level: 2 }).run()}
        class={editor.isActive("heading", { level: 2 }) ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="material-symbols:format-h2" class="editor-icon"/>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleHeading({ level: 3 }).run()}
        class={editor.isActive("heading", { level: 3 }) ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="material-symbols:format-h3" class="editor-icon"/>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleHeading({ level: 4 }).run()}
        class={editor.isActive("heading", { level: 4 }) ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="material-symbols:format-h4" class="editor-icon"/>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleHeading({ level: 5 }).run()}
        class={editor.isActive("heading", { level: 5 }) ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="material-symbols:format-h5" class="editor-icon"/>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleHeading({ level: 6 }).run()}
        class={editor.isActive("heading", { level: 6 }) ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="material-symbols:format-h6" class="editor-icon"/>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleBulletList().run()}
        class={editor.isActive("bulletList") ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="material-symbols:format-list-bulleted-rounded" class="editor-icon"/>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleOrderedList().run()}
        class={editor.isActive("orderedList") ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="material-symbols:format-list-numbered-rounded" class="editor-icon"/>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleCodeBlock().run()}
        class={editor.isActive("codeBlock") ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="ri:code-s-slash-line" class="editor-icon"/>
      </button>
      <button
        on:click={() => editor.chain().focus().toggleBlockquote().run()}
        class={editor.isActive("blockquote") ? "btn btn-xs btn-secondary" : "btn btn-xs"}
      >
        <Icon icon="material-symbols:format-quote" class="editor-icon"/>
      </button>
      <button on:click={() => editor.chain().focus().setHorizontalRule().run()} class="btn btn-xs">
        <Icon icon="material-symbols:horizontal-rule" class="editor-icon"/>
      </button>
      <button on:click={() => editor.chain().focus().setHardBreak().run()} class="btn btn-xs"> <Icon icon="dashicons:editor-break" class="editor-icon"/> </button>
      <button
        on:click={() => editor.chain().focus().undo().run()}
        disabled={!editor.can().chain().focus().undo().run()}
        class="btn btn-xs"
      >
        <Icon icon="material-symbols:undo" class="editor-icon"/>
      </button>
      <button
        on:click={() => editor.chain().focus().redo().run()}
        disabled={!editor.can().chain().focus().redo().run()}
        class="btn btn-xs"
      >
        <Icon icon="material-symbols:redo" class="editor-icon"/>
      </button>
    </div>
  </div>
{/if}
<div bind:this={element} />
