<script lang="ts">
    export let profile = "/images/profile.jpg";
</script>

<div class="navbar bg-base-100">
    <div class="flex-1">
      <a href="/" class="normal-case text-3xl font-bold cursor-pointer tracking-wide text-primary hover:text-primary-focus transition duration-150">LOGO</a>
    </div>
    <div class="flex-none gap-2">
      <div class="form-control">
        <input type="text" placeholder="Search" class="input input-bordered input-sm rounded-full px-3 md:px-5 h-10 w-20 md:w-40" />
      </div>
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