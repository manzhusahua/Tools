import difflib
files_name = ['/mnt/c/Users/v-zhazhai/debug/ttschunk_richland_finesegment/inputdir/chunk_a88053a1ea327e1e8fd25ce7bb313b29_183.audio', '/mnt/c/Users/v-zhazhai/debug/ttschunk_richland_finesegment/inputdir/chunk_a88053a1ea327e1e8fd25ce7bb313b29_183.audio_48k_denoised', '/mnt/c/Users/v-zhazhai/debug/ttschunk_richland_finesegment/inputdir/chunk_a88053a1ea327e1e8fd25ce7bb313b29_183.audio_48k_denoised_24k', '/mnt/c/Users/v-zhazhai/debug/ttschunk_richland_finesegment/inputdir/chunk_a88053a1ea327e1e8fd25ce7bb313b29_183.coarse_segment', '/mnt/c/Users/v-zhazhai/debug/ttschunk_richland_finesegment/inputdir/chunk_a88053a1ea327e1e8fd25ce7bb313b29_183.fine_segment', '/mnt/c/Users/v-zhazhai/debug/ttschunk_richland_finesegment/inputdir/chunk_a88053a1ea327e1e8fd25ce7bb313b29_183.info', '/mnt/c/Users/v-zhazhai/debug/ttschunk_richland_finesegment/inputdir/chunk_a88053a1ea327e1e8fd25ce7bb313b29_183.json', '/mnt/c/Users/v-zhazhai/debug/ttschunk_richland_finesegment/inputdir/chunk_a88053a1ea327e1e8fd25ce7bb313b29_183.richland_result']

chunkaname = "chunk_a88053a1ea327e1e8fd25ce7bb313b29_183.audio"

res = difflib.get_close_matches(chunkaname, files_name, 1, cutoff=0.5)
print(res)