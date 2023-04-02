<script lang="ts">
    import Icon from '@iconify/svelte';
    export let profile = "/images/profile.jpg";
    let search: string;

    $: showSearch = false;
    $: showThemes = false;
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

        {#if showThemes}
          <ul class="dropdown-content menu p-2 shadow bg-base-100 rounded-box mt-4 border border-primary-content">
            <li><button class="btn btn-ghost">Night</button></li>
            <li><button class="btn btn-ghost">Snow</button></li>
            <li><button class="btn btn-ghost">Valentine</button></li>
            <li><button class="btn btn-ghost">Retro</button></li>
            <li><button class="btn btn-ghost">Luxury</button></li>
            <li><button class="btn btn-ghost">Cyberpunk</button></li>
          </ul>
        {/if} 
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