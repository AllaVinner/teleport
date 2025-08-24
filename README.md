# Teleport

<div style="display: flex">
    <img align="left" src="./assets/teleport-icon.png" alt="Teleport Icon" width="128" height="128" style="margin-right: 16px;">
    <div style="display: flex; flex-direction: column; align-item: center">
        <p>A simple CLI teleporting tool.</p>
        <p>Save your favorite paths, and teleport there quickly on demand.</p>
    </div>
</div>
</br>
</br>

## Installation

### From Source
```bash
git clone ...
uv install tool .
```

Add to your `.bashrc` or similar.
```bash
eval $(teleport shell)
```

## Quickstart
```bash
tp init --
tp add my-project "path/to/project"
tp my-project  # Takes your there
tp list --  # List your setup paths
tp remove my-project
tp clear --

```

> [!Note]
> The `--` suffixes are added to make command have more than two arguments. 
> This is how the tool knows if you want to `list` or want to go to your saved path `list`.
> To get around this, one can also use the full CLI name `teleport`.


## Config
Configuration is stored in `~/.config/teleport/teleport.toml`.
This is a basic `toml` file, with a main object `destination`, which is a map between destination name and path.

## Limitation
- Currently not supported to change place of configuration file. 

