import tiktoken

# text = "The self-replicating micro-organisms were unbelievably resilient, even in sub-zero environments."
text = """
Paragraph 1
In the late nineteenth century, scientific discovery began to accelerate in ways that few could have imagined. The spread of telegraph lines, the standardization of time zones, and the first international collaborations created a sense that knowledge itself was becoming global. Laboratories that once worked in isolation started exchanging both instruments and ideas, and an emerging professional class of scientists began to define shared norms for evidence, precision, and reproducibility. The combination of faster communication and new measurement tools turned speculation into data, giving rise to a period of optimism about the power of reason and the universality of physical law.

Paragraph 2
That optimism was tested in the twentieth century as complexity replaced certainty. Physicists confronted quantum indeterminacy, biologists wrestled with genetic variation, and economists realized that perfect markets existed mostly in theory. Each field had to abandon the comfort of deterministic thinking and accept that probability was not ignorance but a fundamental feature of reality. The computer became the emblem of this new perspective: a machine capable of exploring thousands of possibilities in parallel, embracing uncertainty rather than denying it. Modeling, once a simplified sketch of nature, evolved into an engine for understanding emergent behavior.

Paragraph 3
Today, artificial intelligence extends that tradition by giving models the ability to learn from experience. Neural networks can distill patterns from oceans of data, uncovering structures that elude explicit programming. Yet this new power revives old questions about transparency and trust. When an algorithm reaches a conclusion that no human can fully trace, we face the same dilemma that confronted early scientists—how to balance insight with accountability. The future of computational research may depend less on raw accuracy and more on whether we can explain, visualize, and ultimately reason with the machines that now extend our capacity to think.
"""

# Get tokenizers for both models
enc_chat = tiktoken.encoding_for_model("gpt-4o")
enc_embed = tiktoken.encoding_for_model("text-embedding-3-small")

# Encode text
tokens_chat = enc_chat.encode(text)
tokens_embed = enc_embed.encode(text)

# Compare
print("=== GPT-4o ===")
# for t in tokens_chat:
#     print(f"{t:>6}  {enc_chat.decode([t])!r}")

print(f"Total tokens (gpt-4o): {len(tokens_chat)}\n")

print("=== text-embedding-3-small ===")
# for t in tokens_embed:
#     print(f"{t:>6}  {enc_embed.decode([t])!r}")

print(f"Total tokens (embedding model): {len(tokens_embed)}")
