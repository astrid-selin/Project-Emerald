<script lang="ts">
	import TreeOfLife from '$lib/components/TreeOfLife.svelte';
</script>

<svelte:head>
	<title>The Tree of Life - Tarot & Esoteric Knowledge</title>
	<meta
		name="description"
		content="The Kabbalistic Tree of Life showing the 10 Sephiroth and 22 Paths"
	/>
</svelte:head>

<div class="max-w-6xl mx-auto px-4 py-8">
	<!-- Page Header -->
	<div class="text-center mb-8">
		<h1 class="text-4xl font-bold text-gray-900 mb-4">The Tree of Life</h1>
		<p class="text-lg text-gray-600 max-w-3xl mx-auto">
			The Kabbalistic Tree of Life showing the 10 Sephiroth and 22 Paths. Each sphere represents
			a divine emanation, connected by paths that correspond to the 22 letters of the Hebrew
			alphabet and the Major Arcana of the Tarot.
		</p>
	</div>

	<!-- Tree Visualization -->
	<div class="bg-white rounded-lg shadow-lg p-6">
		<TreeOfLife />
	</div>

	<!-- Educational Context -->
	<div class="mt-8 bg-emerald-50 border-l-4 border-emerald-600 p-6 rounded-r-lg">
		<h2 class="text-xl font-semibold text-gray-900 mb-3">About the Tree of Life</h2>
		<div class="prose prose-emerald max-w-none">
			<p class="text-gray-700 mb-3">
				The Tree of Life is a fundamental diagram in Qabalah, representing the creative process
				through which the Divine manifests in the material world. It consists of:
			</p>
			<ul class="list-disc list-inside text-gray-700 space-y-2 ml-4">
				<li>
					<strong>10 Sephiroth:</strong> Divine emanations or spheres, each representing a different
					aspect of God's nature and the cosmos
				</li>
				<li>
					<strong>22 Paths:</strong> Connections between the Sephiroth, corresponding to the 22 Hebrew
					letters and the 22 Major Arcana cards
				</li>
				<li>
					<strong>3 Pillars:</strong> The Pillar of Severity (left), the Pillar of Mercy (right), and
					the Middle Pillar of Equilibrium
				</li>
			</ul>
			<p class="text-gray-700 mt-4">
				Click on any Sephirah to learn more about its correspondences, associated deities, virtues,
				and vices.
			</p>
		</div>
	</div>
</div>
