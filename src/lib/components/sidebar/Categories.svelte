<script lang="ts">
    import Icon from "@iconify/svelte";
</script>

<div class="card w-full border border-primary-content">
    <div class="card-body">
        <h2 class="card-title text-primary border-b border-primary-content pb-5">Categories</h2>
        
        <div class="card w-full mt-5 bg-base-100 border border-primary-content p-3">
            <div class="flex flex-row items-center">
                <Icon icon="mdi:web" class="icon border-2 border-primary rounded-full"/>
                <p class="ml-5">Web dev</p>
            </div>
        </div>
        <div class="card w-full mt-5 bg-base-100 border border-primary-content p-3">
            <div class="flex flex-row items-center">
                <Icon icon="tabler:device-mobile-code" class="icon border-2 border-primary rounded-full"/>
                <p class="ml-5">Mobile dev</p>
            </div>
        </div>
        <div class="card w-full mt-5 bg-base-100 border border-primary-content p-3">
            <div class="flex flex-row items-center">
                <Icon icon="mdi:linux" class="icon border-2 border-primary rounded-full"/>
                <p class="ml-5">Linux</p>
            </div>
        </div>
        <div class="card w-full mt-5 bg-base-100 border border-primary-content p-3">
            <div class="flex flex-row items-center">
                <Icon icon="icon-park-solid:blockchain" class="icon border-2 border-primary rounded-full"/>
                <p class="ml-5">Blockchain</p>
            </div>
        </div>
    </div>
</div>