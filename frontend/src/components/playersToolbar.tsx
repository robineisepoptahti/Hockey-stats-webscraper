import { AppBar, IconButton, Toolbar, Typography } from "@mui/material";
import { Menu as MenuIcon } from "@mui/icons-material";
import "./playersTable.css";

const PlayersToolbar = () => {
  return (
    <AppBar position="static">
      <Toolbar variant="dense">
        <IconButton
          edge="start"
          color="inherit"
          aria-label="menu"
          sx={{ mr: 2 }}
        >
          <MenuIcon />
        </IconButton>
        <Typography variant="h6" color="inherit" component="div">
          Stats
        </Typography>
      </Toolbar>
    </AppBar>
  );
};

export default PlayersToolbar;
