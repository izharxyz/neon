<script lang="ts">
    export let title = "An Amazing Post";
    export let thumbnail = "/images/borg.jpg";
    export let excerpt = "An amazing post which is a must read!";
    // export let time: number = 5;
</script>

<div class="card md:card-side bg-base-100 mt-6">
    <figure class="md:rounded-2xl"><img src={thumbnail} alt="Post" class="object-cover rounded-2xl md:w-64 md:h-64"/></figure>
    <div class="ml-2 md:ml-0 md:card-body">
      <h2 class="mt-6 text-xl font-bold md:card-title">{title}</h2>
      <p class="mt-2">{excerpt}</p>
      <div class="card-actions justify-end">
      </div>
    </div>
</div>