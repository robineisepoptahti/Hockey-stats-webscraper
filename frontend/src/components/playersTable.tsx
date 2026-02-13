import {
  useReactTable,
  getCoreRowModel,
  flexRender,
} from "@tanstack/react-table";
import type { ColumnDef } from "@tanstack/react-table";
import type { Player } from "../types";
import type { PlayersTableProps } from "../types";
import "./playersTable.css";

// Define columns
const columns: ColumnDef<Player>[] = [
  { accessorKey: "name", header: "Player" },
  { accessorKey: "games", header: "Games played" },
  { accessorKey: "goals", header: "Goals" },
  { accessorKey: "assists", header: "Assists" },
  { accessorKey: "points", header: "Points" },
  { accessorKey: "league", header: "League" },
  { accessorKey: "team", header: "Team" },
];

const PlayersTable = ({ players }: PlayersTableProps) => {
  //Tanstack table setup
  const table = useReactTable({
    data: players,
    columns,
    getCoreRowModel: getCoreRowModel(),
  });

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
        {table.getRowModel().rows.map((row) => (
          <tr key={row.id}>
            {row.getVisibleCells().map((cell) => (
              <td key={cell.id}>
                {flexRender(cell.column.columnDef.cell, cell.getContext())}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default PlayersTable;
