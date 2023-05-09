<script lang="ts">
	  import { enhance, type SubmitFunction } from '$app/forms';
    import { page } from '$app/stores';
    import Icon from '@iconify/svelte';
	  import { onMount } from 'svelte';

    export let user: any;
    //export let profile = "/images/profile.jpg";
    let search: string;

    $: showSearch = false;
    let ready = false

    onMount(() => {
      ready = true
    })

    const submitUpdateTheme: SubmitFunction = ({ action }) => {
      const theme = action.searchParams.get('theme')

      if (theme) {
        document.documentElement.setAttribute('data-theme', theme);
      }
    }

    const themes = [
      'night',
      'winter',
      'valentine',
      'retro',
      'forest',
      'luxury',
      'cyberpunk',
      'coffee',
      'dracula'
    ]
</script>

<div class="navbar bg-base-100">
    <div class="flex-1">
      <a href="/" class="logo">NEON</a>
    </div>
    <div class="flex-none gap-2">
      <form class={showSearch? "form-control" : "hidden form-control"} action="/search/{search}">
        <input type="text" placeholder="Search" class="input input-bordered input-secondary w-20 md:w-64 max-w-xs" bind:value={search}/>   
      </form>
      {#if ready}
        <button class="btn " on:click={() => showSearch = !showSearch}>
          <Icon icon="material-symbols:search" class="header-icon"/>
        </button>
      
        <button class="btn dropdown dropdown-end z-50">
          <Icon icon="solar:pallete-2-bold" class="header-icon"/>
          <ul class="dropdown-content menu p-2 shadow bg-base-100 rounded-box mt-4 border border-primary-content">
            <form method="POST" use:enhance={submitUpdateTheme}>
              {#each themes as theme} 
                <li>
                  <button class="btn mt-2" formaction="/?/setTheme&theme={theme}&redirectTo={$page.url.pathname}">
                    {theme}
                  </button>
                </li>
              {/each}
            </form>
          </ul>
        </button>
      {/if}

      {#if user}
        <div class="dropdown dropdown-end">
          <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
          <label tabindex="0" class="btn btn-ghost btn-circle avatar" for="">
            <Icon icon="game-icons:bird-mask" class="icon border-2 border-primary rounded-full"/>
          </label>

          <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
          <ul tabindex="0" class="mt-3 p-2 shadow menu menu-compact dropdown-content bg-base-100 rounded-box w-52">
            <form method="POST">
              <li><a href="/post/create">Create Post</a></li>
              <li><a href="/">Profile</a></li>
              <li><a href="/">Settings</a></li>
              <li><button formaction="/auth/logout" type="submit" class="normal-case">Logout</button></li>
            </form>
          </ul>
        </div> 
      {:else}
        <div>
          <a href="/auth/register"><button class="btn btn-accent">Get Started</button></a>
        </div>
      {/if}
    </div>
  </div>