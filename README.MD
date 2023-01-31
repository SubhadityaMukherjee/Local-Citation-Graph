# Local Citation Graph from Zotero - mermaid + html

- A combination of two repositories. FULL credits go to both of the individual authors : [MikeBergmann](https://github.com/MikeBergmann/graphml2mermaid) , [Jaks6](https://github.com/jaks6/citation_map)
- I just combined all of them in scripts to work together.

## How to use?
- You need Zotero!

### HTML interactive graph
- Clone this repository and cd to it
- Install requirements `pip install -r requirements.txt`
- Select and export papers to `zotero_graph.csv` from Zotero
    - Paste the file in the same directory as this repository
- Run `python3 analyze_papers.py zotero_graph.csv`
- Run `python3 plotter.py`
- This creates files in the `./gephi/` folder
- Open the file `./gephi/visuzalize_graph.html` in your browser

### Mermaid diagram
- Same as before, the mermaid code is automatically copied to the clipboard and shown as output
- Paste the output into [this website](https://mermaid.live/) or any program that supports mermaid. (like Obsidian)