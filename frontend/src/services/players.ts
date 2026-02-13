import axios from "axios";
import type { Player } from "../types";

const baseUrl = import.meta.env.VITE_API_BASE_URL;

const getAll = async () => {
  const response = await axios.get<Player[]>(`${baseUrl}/players`);
  console.log("Received players data:", response.data);
  return response.data;
};

const removePlayer = async (name: string) => {
  const playerList = await getAll();
  const player = playerList.find((p) => p.name === name);
  if (player) {
    const newList = await axios.delete(`${baseUrl}/players/${player.pId}`);
    return newList.status;
  }
};

const addPlayer = async (name: string) => {
  const playerList = await getAll();
  const player = playerList.find((p) => p.name === name);
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
