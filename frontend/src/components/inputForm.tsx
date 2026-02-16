import { TextField, Box, Button } from "@mui/material";
import playerService from "../services/players";
import { useState } from "react";
import type { Player } from "../types";

const InputForm = ({
  setPlayers,
}: {
  setPlayers: (players: Player[] | ((prev: Player[]) => Player[])) => void;
}) => {
  const [text, setText] = useState("");

  const addOnClickListener = () => {
    playerService.addPlayer(text).then((res) => {
      setPlayers(res);
    });
  };
  const removeOnClickListener = () => {
    playerService.removePlayer(text).then(
      (
        res:
          | {
              players: Player[];
              status: number;
            }
          | undefined,
      ) => {
        if (res && res.status === 204) {
          //Filtering manualy, since 204 response doesnt bring a body
          setPlayers(res.players);
        }
      },
    );
  };

  return (
    <Box sx={{ padding: 2 }}>
      <TextField
        label="Player name"
        variant="filled"
        value={text}
        onChange={(e) => setText(e.target.value)}
        fullWidth
      />
      <Button
        onClick={removeOnClickListener}
        variant="contained"
        color="primary"
        sx={{ marginTop: 2, marginRight: 2 }}
      >
        Remove player
      </Button>
      <Button
        onClick={addOnClickListener}
        variant="contained"
        color="primary"
        sx={{ marginTop: 2 }}
      >
        Add player
      </Button>
    </Box>
  );
};

export default InputForm;
