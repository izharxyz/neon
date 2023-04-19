<script lang="ts">
    export let postId: bigint;
    export let title = "An Amazing Post";
    export let thumbnail = "/images/borg.jpg";
    export let excerpt = "An amazing post which is a must read!";
    export let category = "web dev";
    export let time = 5;
    export let slug = ['svelte', 'prisma']
    // export let time: number = 5;
</script>

<div class="card md:card-side bg-base-100 mt-14 md:mt-6">
    <a href="/post/{postId}">
    <figure><img src={thumbnail} alt="Post" class="card md:w-64 md:h-64"/></figure>
    <div class="ml-2 md:ml-0 md:card-body">
        <div class="flex flex-row justify-between">
            <div class="badge badge-outline mt-4 md:mt-0">{category}</div>
            <div class="text-primary-content text-sm mt-3 mr-2 md:mt-0 md:mr-0">{time} mins read</div>
        </div>
        <h2 class="mt-2 text-xl font-bold md:card-title hover:text-primary-focus transition duration-150">{title}</h2>
        <p class="mt-2">{excerpt}</p>
        <div class="card-actions justify-start mt-2 md:mt-0">
            {#each slug as slug}
                <div class="badge badge-secondary"># {slug}</div>
            {/each}
        </div>
    </div>
    </a>
</div>