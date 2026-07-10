(() => {
    const dialog = document.createElement('dialog');
    dialog.className = 'image-preview';
    dialog.innerHTML = '<button class="image-preview-close" type="button" aria-label="Close image preview">&times;</button><img alt="">';
    document.body.appendChild(dialog);

    const previewImage = dialog.querySelector('img');
    const closeButton = dialog.querySelector('button');

    const close = () => dialog.close();
    closeButton.addEventListener('click', close);
    dialog.addEventListener('click', (event) => {
        if (event.target === dialog) close();
    });

    document.addEventListener('click', (event) => {
        const image = event.target.closest('.gallery-item img, .fabric-card img');
        if (!image) return;
        previewImage.src = image.currentSrc || image.src;
        previewImage.alt = image.alt;
        dialog.showModal();
    });
})();
