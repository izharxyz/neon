<script lang="ts">
    import IoIosSearch from 'svelte-icons/io/IoIosSearch.svelte'
    import IoMdColorPalette from 'svelte-icons/io/IoMdColorPalette.svelte'
    export let profile = "/images/profile.jpg";
    let search: string;

    $: showSearch = false;
    $: showThemes = false;
</script>

<div class="navbar bg-base-100">
    <div class="flex-1">
      <a href="/" class="normal-case text-3xl font-bold cursor-pointer tracking-wide text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary">ZEDCODES</a>
    </div>
    <div class="flex-none gap-2">
      <form class={showSearch? "form-control" : "hidden form-control"} action="/search/{search}">
        <input type="text" placeholder="Search" class="input input-bordered input-secondary w-20 md:w-64 max-w-xs" bind:value={search}/>   
      </form>
      <button class="btn" on:click={() => showSearch = !showSearch}>
        <div class="h-7 w-7"><IoIosSearch/></div>
      </button>
      <button class="btn dropdown dropdown-end z-50" on:click={() => showThemes = !showThemes}>
        <div class="h-7 w-7"><IoMdColorPalette/></div>
        <ul class={showThemes? "dropdown-content menu p-2 shadow bg-base-100 rounded-box mt-4 border border-primary-content" : "hidden"}>
            <li><button class="btn btn-ghost">Night</button></li>
            <li><button class="btn btn-ghost">Snow</button></li>
            <li><button class="btn btn-ghost">Valentine</button></li>
            <li><button class="btn btn-ghost">Retro</button></li>
            <li><button class="btn btn-ghost">Luxury</button></li>
            <li><button class="btn btn-ghost">Cyberpunk</button></li>
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