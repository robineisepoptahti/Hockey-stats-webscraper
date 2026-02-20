import {
  useReactTable,
  getCoreRowModel,
  flexRender,
} from "@tanstack/react-table";
import type { ColumnDef } from "@tanstack/react-table";
import type { Player } from "../types";
import type { PlayersTableProps } from "../types";
import type { RemoveResponse } from "../types";
import playersService from "../services/players";
import "./playersTable.css";
import ClearOutlinedIcon from "@mui/icons-material/ClearOutlined";

// Define columns
const columns: ColumnDef<Player>[] = [
  { accessorKey: "name", header: "Player" },
  { accessorKey: "games", header: "Games played" },
  { accessorKey: "goals", header: "Goals" },
  { accessorKey: "assists", header: "Assists" },
  { accessorKey: "points", header: "Points" },
  { accessorKey: "league", header: "League" },
  { accessorKey: "team", header: "Team" },
  {
    header: "Remove",
    cell: ({ row, table }) => (
      <button
        onClick={async () => {
          const updated: RemoveResponse = await playersService.removePlayer(
            row.original.name,
          );
          const meta = table.options.meta as PlayersTableProps;
          meta?.setPlayers(updated.players);
        }}
        style={{
          background: "none",
          border: "none",
          cursor: "pointer",
        }}
      >
        <ClearOutlinedIcon sx={{ color: "red" }} />
      </button>
    ),
  },
];

const PlayersTable = ({ players, setPlayers }: PlayersTableProps) => {
  const safePlayers = Array.isArray(players) ? players : [];

  //Tanstack table setup
  const table = useReactTable({
    data: safePlayers,
    columns,
    getCoreRowModel: getCoreRowModel(),
    meta: { setPlayers },
  });

  const isEmpty = safePlayers.length === 0;

  return (
    <table>
      <thead>
        {table.getHeaderGroups().map((headerGroup) => (
          <tr key={headerGroup.id}>
            {headerGroup.headers.map((header) => (
              <th key={header.id}>
                {flexRender(
                  header.column.columnDef.header,
                  header.getContext(),
                )}
              </th>
            ))}
          </tr>
        ))}
      </thead>
      <tbody>
        {isEmpty ? (
          <tr>
            <td colSpan={columns.length} style={{ textAlign: "center" }}>
              Table empty. Please add player in the input field above.
            </td>
          </tr>
        ) : (
          table.getRowModel().rows.map((row) => (
            <tr key={row.id}>
              {row.getVisibleCells().map((cell) => (
                <td key={cell.id}>
                  {flexRender(cell.column.columnDef.cell, cell.getContext())}
                </td>
              ))}
            </tr>
          ))
        )}
      </tbody>
    </table>
  );
};

export default PlayersTable;
