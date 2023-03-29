<script lang="ts">
    export let profile = "/images/profile.jpg";
    let search: string;
</script>

<div class="navbar bg-base-100">
    <div class="flex-1">
      <a href="/" class="normal-case text-3xl font-bold cursor-pointer tracking-wide text-primary hover:text-primary-focus transition duration-150">ZEDCODES</a>
    </div>
    <div class="flex-none gap-2">
      <form class="hidden md:block form-control" action="/search/{search}">
        <div class="input-group">
          <input type="text" placeholder="Search…" class="input input-bordered" bind:value={search}/>
          <button class="btn btn-square">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
          </button>
        </div>
      </form>
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