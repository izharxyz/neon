<script lang="ts">
    import Icon from "@iconify/svelte";

    export let postId: bigint;
    export let title = "An Amazing Post";
    export let thumbnail = "/images/sky.jpg";
    export let excerpt = "An amazing post which is a must read!";
    export let author = "Zed";
    export let avatar: string | null = null;
    // export let time: number = 5;
</script>

<div class="card w-full bg-base-100 border border-primary-content">
    <a href="/post/{postId}">
    <figure><img src={thumbnail} alt="Shoes" /></figure>
    <div class="card-body">
      <h2 class="card-title hover:text-primary-focus transition duration-150">
        {title}
        <div class="badge badge-secondary">FEATURED</div>
      </h2>
      <p>{excerpt}</p>
      <div class="card-actions justify-between">
        <div class="flex flex-row items-center">
            <div class="avatar">
              {#if avatar}
                <img src={avatar} alt="" class="h-10 w-10 rounded-full">
              {:else}
                <Icon icon="game-icons:bird-mask" class="icon border-2 border-primary rounded-full"/>
              {/if}
            </div>
            <h3 class="ml-4 text-base">
                {author}
            </h3>
        </div> 
        <button class="btn bg-gradient-to-r from-primary to-secondary btn-sm">Read more</button>
      </div>
    </div>
    </a>
  </div>