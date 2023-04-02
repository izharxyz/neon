<script lang="ts">
	  import { enhance, type SubmitFunction } from '$app/forms';
    import { page } from '$app/stores';
    import Icon from '@iconify/svelte';

    export let profile = "/images/profile.jpg";
    let search: string;

    $: showSearch = false;
    $: showThemes = false;

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
      <a href="/" class="logo">ZEDCODES</a>
    </div>
    <div class="flex-none gap-2">
      <form class={showSearch? "form-control" : "hidden form-control"} action="/search/{search}">
        <input type="text" placeholder="Search" class="input input-bordered input-secondary w-20 md:w-64 max-w-xs" bind:value={search}/>   
      </form>
      <button class="btn " on:click={() => showSearch = !showSearch}>
        <Icon icon="material-symbols:search" class="header-icon"/>
      </button>
      <button class="btn dropdown dropdown-end z-50" on:click={() => showThemes = !showThemes}>
        <Icon icon="solar:pallete-2-bold" class="header-icon"/>

        
        <ul class="dropdown-content menu p-2 shadow bg-base-100 rounded-box mt-4 border border-primary-content">
          <form method="POST" use:enhance={submitUpdateTheme}>
            {#each themes as theme} 
              <li>
                <button class="btn btn-ghost" formaction="/?/setTheme&theme={theme}&redirectTo={$page.url.pathname}">
                  {theme}
                </button>
              </li>
            {/each}
          </form>
        </ul>
         
      </button>
      <div class="dropdown dropdown-end">
        <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
        <label tabindex="0" class="btn btn-ghost btn-circle avatar" for="">
          <div class="w-10 rounded-full">
            <img src={profile} alt="profile-pic"/>
          </div>
        </label>

        <!-- svelte-ignore a11y-no-noninteractive-tabindex -->
        <ul tabindex="0" class="mt-3 p-2 shadow menu menu-compact dropdown-content bg-base-100 rounded-box w-52">
          <li>
            <a href="/" class="justify-between">
              Profile
            </a>
          </li>
          <li><a href="/">Settings</a></li>
          <li><a href="/">Logout</a></li>
        </ul>
      </div>
    </div>
  </div>