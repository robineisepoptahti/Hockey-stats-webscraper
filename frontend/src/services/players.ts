import axios from "axios";
import type { Player } from "../types";

const baseUrl = import.meta.env.VITE_API_BASE_URL;

const getAll = async () => {
  const response = await axios.get<Player[]>(`${baseUrl}/players`);
  if (response.status === 200) {
    console.log("Received players data:", response.data);
    return response.data;
  } else {
    console.error(
      "Failed to fetch players data. Status:",
      response.status,
      "Accessing localstorege for cached data.",
    );
    // Cache from localstorage, if backend not available.
    const cache = localStorage.getItem("playersList");
    return cache ? JSON.parse(cache) : [];
  }
};

const removePlayer = async (name: string) => {
  let playerList: Player[] = await getAll();
  const player = playerList.find((p: Player) => p.name === name);
  if (!player) {
    return { players: [], status: 404 };
  }
  const newList = await axios.delete(`${baseUrl}/players/${player.pId}`);
  playerList = playerList.filter((p: Player) => p.name !== name);
  return { players: playerList, status: newList.status };
};

const addPlayer = async (name: string) => {
  const playerList = await getAll();
  const player = playerList.find((p: Player) => p.name === name);
  if (player)
    //Add warning here fo player existing
    return;
  const newList = await axios.post(`${baseUrl}/players`, { name });
  return newList.data;
};

export default {
  getAll,
  removePlayer,
  addPlayer,
};
