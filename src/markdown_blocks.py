def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    for block in blocks:
        if block == '':
            blocks.remove(block)
    for i in range(len(blocks)):
        blocks[i] = blocks[i].strip()

    return blocks