<script lang="ts">
  import StarterKit from "@tiptap/starter-kit";
  import { lowlight } from 'lowlight/lib/core';

  import Paragraph from '@tiptap/extension-paragraph';
  import Heading from '@tiptap/extension-heading';
  import Blockquote from '@tiptap/extension-blockquote';
  import CodeBlockLowlight from '@tiptap/extension-code-block-lowlight';
  import HardBreak from "@tiptap/extension-hard-break";

  import Code from '@tiptap/extension-code';

  import { Editor } from "@tiptap/core";
  import { createEventDispatcher, onMount } from "svelte";

  export let content = ""

  let element: any;
  let editor: any;

  const dispatch = createEventDispatcher()

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
          class: 'whitespace-pre-line',
        },
        }),

        Heading.configure({
          HTMLAttributes: {
            class: 'whitespace-pre-line',
          },
        }),
        HardBreak.configure({
          HTMLAttributes: {
            class: 'this-class-is-useless',
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
      content: `${content}`,

      onUpdate: ({ editor }) => {
        const html = editor.getHTML()
        dispatch('html-change', html)
      }

    });
  });
</script>

<div bind:this={element} />
