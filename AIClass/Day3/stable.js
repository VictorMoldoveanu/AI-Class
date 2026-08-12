import { InferenceClient } from
    "https://cdn.jsdelivr.net/npm/@huggingface/inference@4.13.25/+esm";

const token = "PASTE_YOUR_HUGGING_FACE_TOKEN_HERE";

const client = new InferenceClient(token);

async function generateImage() {
    console.log("Generating image...");

    const imageBlob = await client.textToImage({
        provider: "fal-ai",
        model: "stabilityai/stable-diffusion-xl-base-1.0",
        inputs: "Astronaut riding a horse",
    });

    console.log("Image received:", imageBlob);

    const imageURL = URL.createObjectURL(imageBlob);
    document.getElementById("generated-image").src = imageURL;
}

generateImage().catch((error) => {
    console.error("IMAGE GENERATION FAILED:", error);
});